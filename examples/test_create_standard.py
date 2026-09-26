"""Offline contract tests. Run: python3 -m unittest discover -s examples -p 'test_create_standard.py'."""
import contextlib
import io
import json
import unittest
import urllib.error
import urllib.request
from unittest.mock import patch

from create_standard import NoRedirects, RecipeError, build_payload, create_once, main, validate_base_url

BASE = "https://api.example.com/api/v1"
TOKEN = "fictional-token-never-print"
ID = "11111111-1111-4111-8111-111111111111"


class Reply:
    def __init__(self, status, body):
        self.status = status
        self.body = json.dumps(body).encode()
    def __enter__(self): return self
    def __exit__(self, *args): return None
    def read(self, limit): return self.body[:limit]


class Opener:
    def __init__(self, replies):
        self.replies = list(replies)
        self.calls = []
    def open(self, request, timeout):
        self.calls.append((request, timeout))
        reply = self.replies.pop(0)
        if isinstance(reply, Exception): raise reply
        return reply


class CreateStandardTests(unittest.TestCase):
    def setUp(self):
        self.payload = build_payload("example-encryption")

    def test_dry_run_never_builds_transport_or_requires_token(self):
        stdout, stderr = io.StringIO(), io.StringIO()
        with patch("create_standard.urllib.request.build_opener") as transport, contextlib.redirect_stdout(stdout), contextlib.redirect_stderr(stderr):
            self.assertEqual(main(["--slug", "example-encryption"]), 0)
        transport.assert_not_called()
        self.assertFalse(json.loads(stdout.getvalue())["enabled"])

    def test_one_atomic_inactive_post_and_expected_response(self):
        opener = Opener([Reply(200, {"items": []}), Reply(201, {"id": ID, "slug": self.payload["slug"], "enabled": False, "controlCount": 1})])
        self.assertEqual(create_once(BASE, TOKEN, self.payload, opener)["id"], ID)
        self.assertEqual([req.method for req, _ in opener.calls], ["GET", "POST"])
        req, timeout = opener.calls[1]
        self.assertEqual(req.full_url, BASE + "/standards")
        self.assertEqual(timeout, 30)
        self.assertEqual(req.get_header("Authorization"), "Bearer " + TOKEN)
        body = json.loads(req.data)
        self.assertEqual(body, self.payload)
        self.assertIs(body["enabled"], False)
        self.assertIs(body["controls"][0]["enabled"], False)
        self.assertEqual(body["controls"][0]["autonomy"], "suggest_only")

    def test_existing_slug_never_posts(self):
        opener = Opener([Reply(200, {"items": [{"slug": self.payload["slug"]}]})])
        with self.assertRaisesRegex(RecipeError, "already exists"):
            create_once(BASE, TOKEN, self.payload, opener)
        self.assertEqual(len(opener.calls), 1)

    def test_failed_preflight_never_posts(self):
        opener = Opener([urllib.error.HTTPError(BASE, 401, "unauthorised", {}, io.BytesIO(b"secret"))])
        with self.assertRaisesRegex(RecipeError, "no create request"):
            create_once(BASE, TOKEN, self.payload, opener)
        self.assertEqual(len(opener.calls), 1)

    def test_post_timeout_has_no_retry(self):
        opener = Opener([Reply(200, {"items": []}), TimeoutError("private request context")])
        with self.assertRaisesRegex(RecipeError, "outcome is uncertain") as caught:
            create_once(BASE, TOKEN, self.payload, opener)
        self.assertEqual(len(opener.calls), 2)
        self.assertNotIn(TOKEN, str(caught.exception))
        self.assertNotIn("private", str(caught.exception))

    def test_http_errors_are_safe_and_never_retried(self):
        for status in (403, 409, 422, 500):
            with self.subTest(status=status):
                opener = Opener([Reply(200, {"items": []}), urllib.error.HTTPError(BASE, status, TOKEN, {}, io.BytesIO(TOKEN.encode()))])
                with self.assertRaisesRegex(RecipeError, f"HTTP {status}") as caught:
                    create_once(BASE, TOKEN, self.payload, opener)
                self.assertNotIn(TOKEN, str(caught.exception))
                self.assertEqual(len(opener.calls), 2)

    def test_unexpected_success_response_is_not_confirmed(self):
        for response in ({}, {"id": ID, "slug": self.payload["slug"], "enabled": True, "controlCount": 1}):
            opener = Opener([Reply(200, {"items": []}), Reply(201, response)])
            with self.assertRaisesRegex(RecipeError, "could not be confirmed"):
                create_once(BASE, TOKEN, self.payload, opener)
            self.assertEqual(len(opener.calls), 2)

    def test_redirect_cannot_forward_bearer(self):
        req = urllib.request.Request(BASE, headers={"Authorization": "Bearer " + TOKEN})
        with self.assertRaises(urllib.error.HTTPError):
            NoRedirects().redirect_request(req, None, 302, "redirect", {}, "https://other.example/api/v1")

    def test_bad_targets_rejected(self):
        for url in ("http://api.example.com/api/v1", "https://user:password@example.com/api/v1", "https://example.com/api/v1?token=x", "https://example.com"):
            with self.subTest(url=url), self.assertRaises(RecipeError): validate_base_url(url)
        self.assertEqual(validate_base_url("http://127.0.0.1:8000/api/v1"), "http://127.0.0.1:8000/api/v1")

    def test_enabled_payload_rejected_before_request(self):
        self.payload["controls"][0]["enabled"] = True
        opener = Opener([])
        with self.assertRaisesRegex(RecipeError, "inactive"):
            create_once(BASE, TOKEN, self.payload, opener)
        self.assertEqual(opener.calls, [])


if __name__ == "__main__":
    unittest.main()

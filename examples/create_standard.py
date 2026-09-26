#!/usr/bin/env python3
"""Create one inactive fictional standard. Dry run unless --apply is supplied.

Requires Python 3.10+. No automatic retries, activation or evaluation.
"""
from __future__ import annotations

import argparse
import json
import os
import re
import sys
import urllib.error
import urllib.parse
import urllib.request
import uuid
from typing import Any


class RecipeError(Exception):
    """A safe, user-facing error; never includes credentials or response bodies."""


class NoRedirects(urllib.request.HTTPRedirectHandler):
    def redirect_request(self, req, fp, code, msg, headers, newurl):
        raise urllib.error.HTTPError(req.full_url, code, "Redirect refused", headers, fp)


def build_payload(slug: str) -> dict[str, Any]:
    if not re.fullmatch(r"[a-z0-9][a-z0-9-]{0,159}", slug):
        raise RecipeError("Use a slug of 1–160 lowercase letters, digits or hyphens, starting with a letter or digit.")
    return {
        "name": "Example — encryption review",
        "slug": slug,
        "description": "Fictional documentation example. Review scope and coverage before activation.",
        "enabled": False,
        "controls": [{
            "name": "MDM-enrolled devices report encryption enabled",
            "slug": f"{slug}-encryption",
            "description": "Checks reported encryption; does not prove recovery-key custody.",
            "severity": "medium",
            "category": "Endpoint",
            "autonomy": "suggest_only",
            "enabled": False,
            "parameters": {},
            "definition": {
                "match": {"predicate": "mdm_enrolled_by"},
                "expect": [{"fact": "device_encryption_enabled", "op": "eq", "value": True}],
                "severity": "medium",
                "title": "MDM-enrolled device does not report encryption enabled",
                "evidence": ["mdm_enrolled_by", "device_encryption_enabled"],
            },
        }],
    }


def validate_base_url(value: str) -> str:
    parsed = urllib.parse.urlsplit(value)
    local = parsed.hostname in {"localhost", "127.0.0.1", "::1"}
    if (parsed.scheme != "https" and not (parsed.scheme == "http" and local)) or not parsed.hostname:
        raise RecipeError("Use an HTTPS API base URL; HTTP is allowed only for a local development server.")
    if parsed.username or parsed.password or parsed.query or parsed.fragment:
        raise RecipeError("The API base URL must not contain credentials, a query or a fragment.")
    if parsed.path.rstrip("/") != "/api/v1":
        raise RecipeError("The API base URL must end in /api/v1.")
    return value.rstrip("/")


def request_json(opener, base: str, token: str, path: str, payload=None):
    data = None if payload is None else json.dumps(payload).encode("utf-8")
    request = urllib.request.Request(
        base + path, data=data,
        headers={"Authorization": "Bearer " + token, "Accept": "application/json", "Content-Type": "application/json"},
        method="GET" if data is None else "POST",
    )
    with opener.open(request, timeout=30) as response:
        status = response.status
        raw = response.read(1_048_577)
    if len(raw) > 1_048_576:
        raise ValueError("Response too large")
    return status, json.loads(raw)


def create_once(base: str, token: str, payload: dict[str, Any], opener=None) -> dict[str, str]:
    base = validate_base_url(base)
    if not token or any(char.isspace() for char in token):
        raise RecipeError("Set ALIGNR_ACCESS_TOKEN to a valid short-lived human access token.")
    if payload.get("enabled") is not False or any(c.get("enabled") is not False for c in payload.get("controls", [])):
        raise RecipeError("This example only creates an inactive standard with inactive controls.")
    opener = opener or urllib.request.build_opener(NoRedirects())
    try:
        status, listing = request_json(opener, base, token, "/standards")
        if status != 200 or not isinstance(listing, dict) or not isinstance(listing.get("items"), list):
            raise ValueError("Unexpected standard list")
        if any(not isinstance(item, dict) or "slug" not in item for item in listing["items"]):
            raise ValueError("Unexpected list item")
    except (urllib.error.URLError, OSError, ValueError) as error:
        raise RecipeError("Preflight failed; no create request was sent. Check URL, human token and detection_rule.read access.") from error
    if any(item["slug"] == payload["slug"] for item in listing["items"]):
        raise RecipeError("This standard slug already exists. Inspect it in Standards; no create request was sent.")
    try:
        status, result = request_json(opener, base, token, "/standards", payload)
    except urllib.error.HTTPError as error:
        raise RecipeError(
            f"Create returned HTTP {error.code}. No retry was made. Inspect Standards for slug {payload['slug']} before another write; verify permissions, conflicts or validation errors."
        ) from error
    except (urllib.error.URLError, OSError, ValueError) as error:
        raise RecipeError(
            f"Creation outcome is uncertain. No retry was made. Inspect Standards for slug {payload['slug']} before another write."
        ) from error
    try:
        if status != 201 or not isinstance(result, dict) or result.get("enabled") is not False or result.get("slug") != payload["slug"] or result.get("controlCount") != 1:
            raise ValueError("Unexpected create response")
        standard_id = str(uuid.UUID(result["id"]))
    except (ValueError, KeyError, TypeError, AttributeError) as error:
        raise RecipeError(
            f"Creation could not be confirmed from the response. Inspect Standards for slug {payload['slug']}; do not retry blindly."
        ) from error
    return {"id": standard_id, "slug": result["slug"], "state": "inactive"}


def main(argv=None) -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--slug", required=True, help="A stable new slug to locate the draft after this request.")
    parser.add_argument("--api-base", help="Your intended environment, ending in /api/v1; required with --apply.")
    parser.add_argument("--apply", action="store_true", help="Send one create request after the read-only preflight.")
    args = parser.parse_args(argv)
    try:
        payload = build_payload(args.slug)
        if not args.apply:
            print(json.dumps(payload, indent=2))
            print("Dry run: no requests sent. Review this payload before using --apply.", file=sys.stderr)
            return 0
        if not args.api_base:
            raise RecipeError("--apply requires an explicit --api-base for the intended environment.")
        result = create_once(args.api_base, os.environ.get("ALIGNR_ACCESS_TOKEN", ""), payload)
        print(json.dumps(result, indent=2))
        print("Open this standard in Alignr and verify its inactive control. No activation or evaluation was requested.")
        return 0
    except RecipeError as error:
        print(str(error), file=sys.stderr)
        return 1


if __name__ == "__main__":
    raise SystemExit(main())

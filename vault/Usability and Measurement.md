# Usability and measurement

## What has been done

On 26 September 2026, the coordinator used agent-browser to navigate the real local demo app (source 858bcaf, with concurrent worker-only changes) and published docs. Captured six genuine screenshots of setup, assistant, client checks and reports, reviewed them for unwanted personal/credential content, and created an 18-second slideshow with a text transcript. It is explicitly a screen tour, not footage of completed authorisation or AI execution. Seeded Northwind Dental and Apex Healthcare are fictional; empty/unverified states are intentionally preserved.

The local recorder restarts browser context and lost the in-memory sign-in session. Its login-only recording was discarded outside the repository; no login video or credentials are published. Screen images remain unaltered. Mintlify stripped the nested video track element during preview, so the public page includes an adjacent time-coded text transcript instead of promising unavailable player captions. Public captions identify local demo state and the unconfigured shared Microsoft application.

This was an agent-led walkthrough, not a study with independent humans. No conversion lift, completion-time improvement or successful vendor onboarding was measured.

## Observed documentation findings

| Task | Observation | Change / next verification |
| --- | --- | --- |
| Find setup for a non-GDAP client | Live search `non gdap` returned the partner-delegated entry first and the client connection guide second. | Added explicit Direct (non-GDAP) wording to the existing client guide; preserve its anchor. Recheck indexing after publication. |
| Find teammate invitations | Live search `invite teammates` returned general journeys/setup before the account/team page, which was absent from the six shown results. | Renamed the page to Manage your account and invite teammates. After release 5502799, the same live query returned it first. This is one query observation, not a general search-quality or conversion claim. |
| Find report preparation in the app | Client More menu exposes Review reports; report screen has name + Prepare review. | Added real screen and textual callouts to visual tour. No report created. |
| Recognise incomplete setup | Demo has no shared Microsoft app, unverified evidence and never-run controls. | Captions explain these states; no simulated passing assessment. |
| Run a write recipe with an API key | Endpoint depends on human JWT rather than API-key dependency. | New recipe explicitly requires human access, defaults to dry run and makes one POST only. |

## Human study ready to run

Recruit consenting people unfamiliar with Alignr: an MSP administrator, technician and account manager. Recruitment/messages are not sent by this change. Use an authorised demo workspace. Ask permission before recording; keep participant identities and raw recordings out of this public repository. Use participant codes in the worksheet.

Give a goal, not the click sequence. Start at docs Introduction. Let the participant choose search or navigation. Stop a task before entering real credentials, consenting to vendor access, inviting people, changing billing or applying a production action unless separately authorised for that session.

| ID | Participant task | Observable completion |
| --- | --- | --- |
| U01 | Find how to start with one client and know whether the pilot worked. | Explains pilot checkpoints and global activation boundary. |
| U02 | Set up a Microsoft client absent from Partner Center. | Finds Direct path and identifies tenant/admin-consent verification. |
| U03 | Invite a technician with appropriate access. | Finds account/team guide and explains roles and invitation acceptance. |
| U04 | Explain a control that needs evidence. | Distinguishes collection from evaluation and names next investigation. |
| U05 | Ask the assistant to change one client's threshold. | Checks scope, Before/After and explicit apply; reassessment remains separate. |
| U06 | Prepare a client discussion and record a decision. | Finds report/meeting guide, distinguishes snapshot and portal, names owner and verification. |
| U07 | Find AI data handling and request deletion information. | Finds security guide and identifies which commitments need authoritative terms. |
| U08 | Preview creation of an inactive standard. | Runs dry-run example without token/network; identifies human-token requirement before applying. |

Record outcome as completed, assisted, blocked or abandoned; preserve the distinction. Record elapsed seconds, pages visited, search terms, misinterpretations, help given and the exact stop point. An observer intervening changes the outcome to assisted. Summarise by task, role and device; report the sample size and do not infer broad conversion effects from a few sessions.

## Measurement worksheet and review loop

Use `vault/Review Evidence/usability-sessions.csv`. It is an empty template, not fabricated evidence. `scripts/summarize-usability.py` validates and summarises its rows, reporting completed/assisted/blocked/abandoned separately and the median duration of completed tasks. Do not store names, emails, client records or raw search text containing secrets.

Each release: inspect new search failures and feedback, reproduce one high-impact failure, fix it, then rerun that task. Each week: review task completion and the most frequent unanswered questions with the documentation owner. The cadence is an operating instruction, not an automated scheduled job.

## Mintlify analytics

Current official documentation describes search query volume, no-result queries, result click-through, engagement and feedback. Analytics and feedback require the relevant Mintlify plan; feedback must be enabled in dashboard Add-ons. This session did not authenticate to the Mintlify dashboard or verify subscription entitlement, so collection/export access is UNVERIFIED. No third-party analytics tracker or paid add-on was installed.

When access is available, review Search and Feedback for a fixed date range and retain aggregate findings, not raw identifiable conversations. Search click-through measures result clicks, not successful task completion; asking the assistant is not counted as a search-result click. Use human task observations alongside it. Native search data cannot by itself establish an app signup or assessment-completion conversion.

Sources checked 2026-09-26: [analytics](https://www.mintlify.com/docs/analytics), [search](https://www.mintlify.com/docs/analytics/search), [feedback](https://www.mintlify.com/docs/optimize/feedback). Keep any export/warehouse delivery subject to the applicable access and data-handling policy. User authorised documentation improvements; this is not authority to publish personal analytics or invent policy commitments.

## Outstanding external evidence

- Consenting human participants and actual study results.
- Authorised vendor test environments for end-to-end consent and collection acceptance.
- Approved pricing, privacy, retention, subprocessor and service documents; requested from the owner during this task.
- Authenticated Mintlify dashboard access/entitlement to confirm analytics and feedback configuration.

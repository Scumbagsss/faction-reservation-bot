# Faction Reservation & Review Workflow — architecture notes

> This is a **suggested technical boundary for a private-source module**, not a claim that all components are implemented or active in a particular deployment.

## Objective

Group/faction applications in RP communities often involve a limited resource: one reservation or a finite set of places. Staff need a consistent way to review applications, prevent conflicting reservations and communicate a final outcome.

## Conceptual responsibilities

**1. Faction selector.** Display the eligible factions and their current availability.

**2. Application form.** Collect a structured reservation request.

**3. Conflict check.** Check that an active reservation does not conflict with the request.

**4. Staff review.** Route the application to authorized staff for a recorded decision.

**5. State and notification.** Update the faction state and notify the applicant.

## Review risks and recommended tests

| Concern | Failure mode | Verification to add |
|---|---|---|
| Competing claims | Two applicants may reserve the same faction simultaneously | Use atomic unique state or compare-and-swap |
| Expired requests | A stale pending case may block a faction indefinitely | Define expiry and recovery policy |
| Reviewer permissions | Faction-specific staff permissions may differ | Verify at review time and test role changes |
| Applicant identity | A notification or Discord message can disappear | Store request state independently of UI |

## Integration and permissions

The Discord interaction layer should treat its inputs as untrusted. A server-side handler must establish the principal, check authorization for the concrete operation and return user-safe errors. The persistence or external API adapter is separately responsible for safe updates, retries and recovery. The public `src/public_interface.py` is only a surface sketch; **none of these safeguards can be confirmed by running it**.

## Production/public boundary

No real member IDs, credentials, channel IDs, private schemas, moderation rules or live logs should appear in this repository. The architectural context belongs to the wider [DeadCity platform case study](https://github.com/Scumbagsss/BOT). For a separately developed runnable example, see the [ticket workflow backend](https://github.com/Scumbagsss/advanced-discord-ticket-bot).

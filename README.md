# Faction Reservation Bot

> **Portfolio showcase — production source is private and this repository is intentionally non-runnable.**

Faction reservation and application workflow for RP/game communities with staff review.

## What it demonstrates

- Faction selection menu
- Application forms
- Staff approve/reject/reserve workflow
- Reason modals
- Applicant notifications
- Faction management panel

## Technology

Python • discord.py • Persistent Views • JSON storage

## High-level workflow

1. Player selects faction
2. Submit reservation application
3. Route to staff review
4. Apply decision
5. Update persistent faction state

## Public interface preview

The public skeleton exposes only the architectural surface:

- `open_reservation(...)`
- `submit_application(...)`
- `review_application(...)`
- `update_faction_state(...)`

The production implementations behind these methods are withheld. See [`NOTICE.md`](NOTICE.md).

## Repository contents

- `src/public_interface.py` — non-runnable interface skeleton;
- `docs/ARCHITECTURE.md` — high-level design;
- `examples/config.example.jsonc` — sanitized configuration shape;
- `LICENSE` — explicit all-rights-reserved notice.

## Status

Production-tested private project / portfolio edition.

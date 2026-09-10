"""Portfolio-only interface skeleton. This module is intentionally non-runnable."""


class FactionReservationBotInterface:
    """Architectural surface of the private production implementation."""

    async def open_reservation(self, *args, **kwargs):
        """Public portfolio signature only. Production logic is private."""
        raise NotImplementedError("Production implementation is private")

    async def submit_application(self, *args, **kwargs):
        """Public portfolio signature only. Production logic is private."""
        raise NotImplementedError("Production implementation is private")

    async def review_application(self, *args, **kwargs):
        """Public portfolio signature only. Production logic is private."""
        raise NotImplementedError("Production implementation is private")

    async def update_faction_state(self, *args, **kwargs):
        """Public portfolio signature only. Production logic is private."""
        raise NotImplementedError("Production implementation is private")


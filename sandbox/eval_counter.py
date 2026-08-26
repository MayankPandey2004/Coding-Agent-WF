class Counter:
    """A simple counter that starts at 0 and can be incremented or decremented."""

    def __init__(self):
        self._count = 0

    def increment(self, step: int = 1) -> None:
        """Increase the counter by *step* (default 1)."""
        self._count += step

    def decrement(self, step: int = 1) -> None:
        """Decrease the counter by *step* (default 1)."""
        self._count -= step

    def value(self) -> int:
        """Return the current count value."""
        return self._count

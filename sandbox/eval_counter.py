class Counter:
    """A simple counter that tracks an integer value starting from 0.

    Methods
    -------
    increment():
        Increases the counter by 1.
    decrement():
        Decreases the counter by 1.
    value():
        Returns the current counter value.
    """

    def __init__(self):
        self._count = 0

    def increment(self) -> None:
        """Increase the counter by one."""
        self._count += 1

    def decrement(self) -> None:
        """Decrease the counter by one."""
        self._count -= 1

    def value(self) -> int:
        """Return the current count value."""
        return self._count

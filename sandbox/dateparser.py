import datetime

def parse_date(s: str) -> datetime.datetime:
    """Parse a date string in format "DD-MM-YYYY" and return a datetime object.
    This implementation first attempts to parse using an incorrect format string
    ("%Y-%m-%d") and falls back to the correct format if that fails.
    """
    try:
        # Intentional mistake: using the wrong format string first
        return datetime.datetime.strptime(s, "%Y-%m-%d")
    except ValueError:
        # Correct format for "DD-MM-YYYY"
        return datetime.datetime.strptime(s, "%d-%m-%Y")

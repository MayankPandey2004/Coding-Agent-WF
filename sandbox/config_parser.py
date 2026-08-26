# Compatibility import for tomllib (Python 3.11+) with fallback to tomli for older versions.
try:
    import tomllib  # Python 3.11+
except ModuleNotFoundError:  # pragma: no cover
    import tomli as tomllib  # type: ignore

from typing import Any

def get_config_value(toml_str: str, key_path: str) -> Any:
    """Parse a TOML configuration string and return the value for a nested key.

    Args:
        toml_str: The TOML configuration as a string.
        key_path: Dot‑separated path to the desired key, e.g. "database.host".

    Returns:
        The value associated with the given key path.

    Raises:
        KeyError: If any part of the path does not exist.
        tomllib.TOMLDecodeError: If the TOML string cannot be parsed.
    """
    # Parse the TOML string into a Python dict
    config = tomllib.loads(toml_str)

    # Traverse the nested dictionaries according to the dot‑separated key_path
    parts = key_path.split('.')
    current: Any = config
    for part in parts:
        if isinstance(current, dict) and part in current:
            current = current[part]
        else:
            raise KeyError(f"Key path '{key_path}' not found (stuck at '{part}')")
    return current

import pytest
from config_parser import get_config_value

@pytest.fixture
def sample_toml():
    return """
[database]
host = "localhost"
port = 5432
[server]
address = "0.0.0.0"
port = 8080
"""

def test_get_existing_key(sample_toml):
    assert get_config_value(sample_toml, "database.host") == "localhost"
    assert get_config_value(sample_toml, "database.port") == 5432
    assert get_config_value(sample_toml, "server.address") == "0.0.0.0"
    assert get_config_value(sample_toml, "server.port") == 8080

def test_missing_key(sample_toml):
    with pytest.raises(KeyError):
        get_config_value(sample_toml, "database.username")
    with pytest.raises(KeyError):
        get_config_value(sample_toml, "api.key")

def test_invalid_toml():
    bad_toml = "[invalid\nkey = 'value'"
    with pytest.raises(Exception):  # tomllib.TOMLDecodeError is a subclass of Exception
        get_config_value(bad_toml, "any.key")

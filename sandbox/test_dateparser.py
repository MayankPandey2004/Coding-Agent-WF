import datetime
import pytest
from dateparser import parse_date

def test_parse_date_year():
    dt = parse_date("25-12-2026")
    assert dt.year == 2026

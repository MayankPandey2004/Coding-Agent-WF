import pytest
from eval_reverse import reverse_words

def test_reverse_basic():
    assert reverse_words("hello world") == "world hello"

def test_multiple_spaces():
    # multiple spaces should be normalized to single spaces per spec
    assert reverse_words("  a   b c  ") == "c b a"

def test_empty_string():
    assert reverse_words("") == ""

def test_non_string():
    with pytest.raises(TypeError):
        reverse_words(123)

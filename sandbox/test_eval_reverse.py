import pytest
from eval_reverse import reverse_words

def test_reverse_words_basic():
    assert reverse_words("hello world") == "world hello"
    assert reverse_words("The quick brown fox") == "fox brown quick The"

def test_reverse_words_single_word():
    assert reverse_words("hello") == "hello"

def test_reverse_words_empty_string():
    assert reverse_words("") == ""

def test_reverse_words_whitespace():
    assert reverse_words("   hello   world   ") == "world hello"
    assert reverse_words("   ") == ""

def test_reverse_words_type_error():
    with pytest.raises(TypeError):
        reverse_words(123)

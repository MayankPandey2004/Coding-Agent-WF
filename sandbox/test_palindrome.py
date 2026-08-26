import pytest
from palindrome import is_palindrome

def test_empty_string():
    assert is_palindrome("") is True

def test_single_character():
    assert is_palindrome("a") is True

def test_valid_palindromes():
    assert is_palindrome("racecar") is True
    assert is_palindrome("noon") is True
    assert is_palindrome("kayak") is True
    assert is_palindrome("madam") is True
    assert is_palindrome("12321") is True

def test_non_palindromes():
    assert is_palindrome("hello") is False
    assert is_palindrome("python") is False
    assert is_palindrome("ab") is False
    assert is_palindrome("12345") is False

def test_case_sensitivity():
    # Strict case sensitivity check
    assert is_palindrome("Racecar") is False
    assert is_palindrome("Madam") is False

def test_with_spaces_and_punctuation():
    assert is_palindrome("race car") is False
    assert is_palindrome("n o o n") is True

def test_invalid_input_type():
    with pytest.raises(TypeError):
        is_palindrome(12321)  # type: ignore
    with pytest.raises(TypeError):
        is_palindrome(None)  # type: ignore

import pytest
from eval_dedupe import dedupe_preserve_order

def test_dedupe_preserve_order_basic():
    assert dedupe_preserve_order([1, 2, 3, 2, 1, 4]) == [1, 2, 3, 4]

def test_dedupe_preserve_order_strings():
    assert dedupe_preserve_order(["a", "b", "a", "c", "b"]) == ["a", "b", "c"]

def test_dedupe_preserve_order_empty():
    assert dedupe_preserve_order([]) == []

def test_dedupe_preserve_order_no_dups():
    assert dedupe_preserve_order([1, 2, 3]) == [1, 2, 3]

def test_dedupe_preserve_order_all_dups():
    assert dedupe_preserve_order([5, 5, 5, 5]) == [5]

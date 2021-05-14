import pytest
import wordCount

def test_count():
    assert wordCount.count('Hello, my name is mike') == 5
    assert wordCount.count('Hello') == 1
    assert wordCount.count(5) == "Invalid Input"
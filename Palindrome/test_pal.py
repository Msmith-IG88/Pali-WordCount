import pytest
import palindrome

def test_pal():
    assert palindrome.pal('madam') == "Is Palindrome"
    assert palindrome.pal('teacher') == "Not Palindrome"
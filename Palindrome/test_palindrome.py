import unittest
import palindrome

class test(unittest.TestCase):
    def test_control(self):
        result = palindrome.pal('racecar')
        self.assertEqual(result, "Is Palindrome")

    def test_nonPal(self):
        result = palindrome.pal('teacher')
        self.assertEqual(result, "Not Palindrome")

    def test_invalidInput(self):
        result = palindrome.pal(5)
        self.assertEqual(result, "Invalid Input")
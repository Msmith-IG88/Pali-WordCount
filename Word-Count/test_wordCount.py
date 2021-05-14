import unittest
import wordCount

class test(unittest.TestCase):
    def test_control(self):
        result = wordCount.count('Hello, my name is Mike.')
        self.assertEqual(result, 5)

    def test_oneWord(self):
        result = wordCount.count('Hello')
        self.assertEqual(result, 1)

    def test_error(self):
        result = wordCount.count(5)
        self.assertEqual(result, "Invalid Input")
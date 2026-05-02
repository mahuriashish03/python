import unittest
from practice.testing import cap

class TestCap(unittest.TestCase):
    def test_one_word(self):
        text = "python"
        result = cap.cap_text(text)
        self.assertEqual(result, "Python")

    def test_two_words(self):
        text = "i love python"
        result = cap.cap_text(text)
        self.assertEqual(result, "I Love Python")

if __name__ == "__main__":
    unittest.main()

# run this file: python .\practice\testing\test_cap.py
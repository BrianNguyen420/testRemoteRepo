import unittest
from addition import addition

class TestAdditionFuction(unittest.TestCase):
    def test_addTwoNumberCase1(self):
        self.assertEqual(addition(2, 3), 5, "Error: additional result is incorrect.")

    def test_addTwoNumberCase2(self):
        self.assertEqual(addition(3, -3), 0, "Error: additional result is incorrect.")
        
    def test_addTwoNumberCase3(self):
        self.assertEqual(addition(3, -1), 2, "Error: additional result is incorrect.")

if __name__ == "__main__":
    unittest.main()


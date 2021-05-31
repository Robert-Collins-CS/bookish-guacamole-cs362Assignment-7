import unittest
import fizzbuzz


class TestStringMethods(unittest.TestCase):

    def test_fizzbuzz(self):
        testList = fizzbuzz.populateList()
        self.assertTrue(testList[3] == "Buzz")


if __name__ == '__main__':
    unittest.main()

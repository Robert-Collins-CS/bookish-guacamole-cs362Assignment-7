import unittest
import fizzbuzz


class TestStringMethods(unittest.TestCase):

    def test_fizzbuzz(self):
        testList = fizzbuzz.fizzBuzz((fizzbuzz.populateList()))
        self.assertTrue(testList[2] == "Fizz")


if __name__ == '__main__':
    unittest.main()

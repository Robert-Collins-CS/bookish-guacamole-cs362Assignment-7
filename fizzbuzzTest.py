import unittest
import fizzbuzz


class TestStringMethods(unittest.TestCase):

    def test_fizz(self):
        testList = fizzbuzz.fizzBuzz((fizzbuzz.populateList()))
        self.assertTrue(testList[2] == "Fizz")
        
    
    def test_fizzbuzz(self):
        testList = fizzbuzz.fizzBuzz((fizzbuzz.populateList()))
        self.assertEqual(testList[14], "FizzBuzz")


if __name__ == '__main__':
    unittest.main()

import unittest
import newLeapYear as nLYear


class TestStringMethods(unittest.TestCase):

    def test_checkNotLeap(self):
        leapBool = nLYear.checkLeap(3000)
        self.assertFalse(leapBool)

    def test_checkLeap(self):
        leapBool = nLYear.checkLeap(4000)
        self.assertTrue(leapBool)
        
        
if __name__ == '__main__':
    unittest.main()

import unittest
import newLeapYear as nLYear


class TestStringMethods(unittest.TestCase):

    def test_checkLeap(self):
        leapBool = nLYear.checkLeap(3000)
        self.assertFalse(leapBool)

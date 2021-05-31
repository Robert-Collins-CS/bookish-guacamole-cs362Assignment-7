import unittest
import newLeapYear as nLYear


class TestStringMethods(unittest.TestCase):

    def test_checkLeap(self):
        leapBool = nLYear.checkLeap(2000)
        self.assertFalse(leapBool)

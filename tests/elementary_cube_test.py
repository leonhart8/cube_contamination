import unittest
import elementary_cube as ec


class MyTestCase(unittest.TestCase):
    """
    Test suite of the ElementaryCube class
    """

    def setUp(self):
        """
        Method which sets up the objects that will be used throughout the test suite
        :return: AssertionError or SkipTest
        """
        self.ec = ec.ElementaryCube()

    def test_get_contamination_state_returns_contamination_state(self):
        """
        Check if the elementary cube's getter for the contamination state does indeed
        return the cube's current contamination state
        :return: AssertionError if the test fails, None otherwise
        """
        self.assertFalse(self.ec.get_contamination_state())

    def test_contaminates_changes_contamination_state(self):
        """
        Checks that the contamination method does indeed change the contamination state
        :return: AssertionError if the test fails, None otherwise
        """
        self.ec.contaminate()
        self.assertTrue(self.ec.get_contamination_state())


if __name__ == '__main__':
    unittest.main()

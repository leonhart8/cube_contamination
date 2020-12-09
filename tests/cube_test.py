import unittest
import cube

class MyTestCase(unittest.TestCase):
    """
    Test class for the cube class
    """

    def setUp(self):
        """
        Method which sets up the cube that will be used for further testing
        :return: AssertionError if the setup fails, Nothing otherwise
        """
        self.cube = cube.Cube(5)


if __name__ == '__main__':
    unittest.main()

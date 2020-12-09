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

    # Start by testing neighbors for elementary cubes in contact with 0 sides of the bigger cube

    def test_get_neighbors_for_middle_cube(self):
        """
        Checks if the neighbors of a "middle" cube with four neighbors are the correct ones
        :return: AssertionError if the setup fails, Nothing otherwise
        """
        s = {(2, 2, 1), (2, 2, 3), (2, 1, 2), (2, 3, 2), (1, 2, 2), (3, 2, 2)}
        self.assertEqual(s, self.cube.get_neighbors(2, 2, 2))

    # Testing neighbors for elementary cubes in contact with 1 side of the bigger cube

    def test_get_neighbors_for_left_side(self):
        """
        Checks for the right neighbors for an elementary cube in contact
        with the left side of the cube
        :return: AssertionError if the setup fails, Nothing otherwise
        """
        s = {(1, 2, 2), (0, 1, 2), (0, 3, 2), (0, 2, 1), (0, 2, 3)}
        self.assertEqual(s, self.cube.get_neighbors(0, 2, 2))

    def test_get_neighbors_for_right_side(self):
        """
        Checks for the right neighbors for an elementary cube in contact
        with the right side of the cube
        :return: AssertionError if the setup fails, Nothing otherwise
        """
        s = {(3, 2, 2), (4, 1, 2), (4, 3, 2), (4, 2, 1), (4, 2, 3)}
        self.assertEqual(s, self.cube.get_neighbors(4, 2, 2))

    def test_get_neighbors_for_back_side(self):
        """
        Checks for the right neighbors for an elementary cube in contact
        with the right side of the cube
        :return: AssertionError if the setup fails, Nothing otherwise
        """
        s = {(1, 2, 4), (3, 2, 4), (2, 1, 4), (2, 3, 4), (2, 2, 3)}
        self.assertEqual(s, self.cube.get_neighbors(2, 2, 4))

    def test_get_neighbors_for_front_side(self):
        """
        Checks for the right neighbors for an elementary cube in contact
        with the front side of the cube
        :return: AssertionError if the setup fails, Nothing otherwise
        """
        s = {(1, 2, 0), (3, 2, 0), (2, 1, 0), (2, 3, 0), (2, 2, 1)}
        self.assertEqual(s, self.cube.get_neighbors(2, 2, 0))

    def test_get_neighbors_for_bottom_side(self):
        """
        Checks for the right neighbors for an elementary cube in contact
        with the bottom side of the cube
        :return: AssertionError if the setup fails, Nothing otherwise
        """
        s = {(1, 0, 2), (3, 0, 2), (2, 1, 2), (2, 0, 1), (2, 0, 3)}
        self.assertEqual(s, self.cube.get_neighbors(2, 0, 2))

    def test_get_neighbors_for_top_side(self):
        """
        Checks for the right neighbors for an elementary cube in contact
        with the top side of the cube
        :return: AssertionError if the setup fails, Nothing otherwise
        """
        s = {(1, 4, 2), (3, 4, 2), (2, 3, 2), (2, 4, 1), (2, 4, 3)}
        self.assertEqual(s, self.cube.get_neighbors(2, 4, 2))

    # Testing neighbors for elementary cubes in contact with 2 sides of the bigger cube

    def test_get_neighbors_for_left_front_side(self):
        """
        Checks for the right neighbors for an elementary cube in contact
        with the left and front side of the cube
        :return: AssertionError if the setup fails, Nothing otherwise
        """
        s = {(1, 2, 0), (0, 1, 0), (0, 3, 0), (0, 2, 1)}
        self.assertEqual(s, self.cube.get_neighbors(0, 2, 0))

    def test_get_neighbors_for_left_back_side(self):
        """
        Checks for the right neighbors for an elementary cube in contact
        with the left and back side of the cube
        :return: AssertionError if the setup fails, Nothing otherwise
        """
        s = {(1, 2, 4), (0, 1, 4), (0, 3, 4), (0, 2, 3)}
        self.assertEqual(s, self.cube.get_neighbors(0, 2, 4))

    def test_get_neighbors_for_left_top_side(self):
        """
        Checks for the right neighbors for an elementary cube in contact
        with the left and top side of the cube
        :return: AssertionError if the setup fails, Nothing otherwise
        """
        s = {(1, 4, 2), (0, 3, 2), (0, 4, 1), (0, 4, 3)}
        self.assertEqual(s, self.cube.get_neighbors(0, 4, 2))

    def test_get_neighbors_for_left_bottom_side(self):
        """
        Checks for the right neighbors for an elementary cube in contact
        with the left and bottom side of the cube
        :return: AssertionError if the setup fails, Nothing otherwise
        """
        s = {(1, 0, 2), (0, 1, 2), (0, 0, 1), (0, 0, 3)}
        self.assertEqual(s, self.cube.get_neighbors(0, 0, 2))

    def test_get_neighbors_for_right_front_side(self):
        """
        Checks for the right neighbors for an elementary cube in contact
        with the right and front side of the cube
        :return: AssertionError if the setup fails, Nothing otherwise
        """
        s = {(3, 2, 0), (4, 1, 0), (4, 3, 0), (4, 2, 1)}
        self.assertEqual(s, self.cube.get_neighbors(4, 2, 0))

    def test_get_neighbors_for_right_back_side(self):
        """
        Checks for the right neighbors for an elementary cube in contact
        with the right and back side of the cube
        :return: AssertionError if the setup fails, Nothing otherwise
        """
        s = {(3, 2, 4), (4, 1, 4), (4, 3, 4), (4, 2, 3)}
        self.assertEqual(s, self.cube.get_neighbors(4, 2, 4))

    def test_get_neighbors_for_right_top_side(self):
        """
        Checks for the right neighbors for an elementary cube in contact
        with the right and top side of the cube
        :return: AssertionError if the setup fails, Nothing otherwise
        """
        s = {(3, 4, 2), (4, 3, 2), (4, 4, 1), (4, 4, 3)}
        self.assertEqual(s, self.cube.get_neighbors(4, 4, 2))

    def test_get_neighbors_for_right_bottom_side(self):
        """
        Checks for the right neighbors for an elementary cube in contact
        with the right and top side of the cube
        :return: AssertionError if the setup fails, Nothing otherwise
        """
        s = {(3, 0, 2), (4, 1, 2), (4, 0, 1), (4, 0, 3)}
        self.assertEqual(s, self.cube.get_neighbors(4, 0, 2))

    def test_get_neighbors_for_back_top_side(self):
        """
        Checks for the right neighbors for an elementary cube in contact
        with the back and top side of the cube
        :return: AssertionError if the setup fails, Nothing otherwise
        """
        s = {(1, 4, 4), (3, 4, 4), (2, 3, 4), (2, 4, 3)}
        self.assertEqual(s, self.cube.get_neighbors(2, 4, 4))

    def test_get_neighbors_for_back_bottom_side(self):
        """
        Checks for the right neighbors for an elementary cube in contact
        with the back and bottom side of the cube
        :return: AssertionError if the setup fails, Nothing otherwise
        """
        s = {(1, 0, 4), (3, 0, 4), (2, 1, 4), (2, 0, 3)}
        self.assertEqual(s, self.cube.get_neighbors(2, 0, 4))

    def test_get_neighbors_for_front_top_side(self):
        """
        Checks for the right neighbors for an elementary cube in contact
        with the front and top side of the cube
        :return: AssertionError if the setup fails, Nothing otherwise
        """
        s = {(1, 4, 0), (3, 4, 0), (2, 3, 0), (2, 4, 1)}
        self.assertEqual(s, self.cube.get_neighbors(2, 4, 0))

    def test_get_neighbors_for_front_bottom_side(self):
        """
        Checks for the right neighbors for an elementary cube in contact
        with the front and bottom side of the cube
        :return: AssertionError if the setup fails, Nothing otherwise
        """
        s = {(1, 0, 0), (3, 0, 0), (2, 1, 0), (2, 0, 1)}
        self.assertEqual(s, self.cube.get_neighbors(2, 0, 0))

    # Testing for elementary cubes in contact with 3 other sides

    def test_get_neighbors_for_front_top_left_corner(self):
        """
        Checks for the right neighbors for an elementary cube in contact
        with the front, top left corner of the cube
        :return: AssertionError if the setup fails, Nothing otherwise
        """


    def test_get_neighbors_for_front_top_right_corner(self):
        """
        Checks for the right neighbors for an elementary cube in contact
        with the front, top right corner of the cube
        :return: AssertionError if the setup fails, Nothing otherwise
        """
        s = {(1, 4, 0), (0, 3, 0), (0, 4, 1)}
        self.assertEqual(s, self.cube.get_neighbors(0, 4, 0))

    def test_get_neighbors_for_front_bottom_left_corner(self):
        """
        Checks for the right neighbors for an elementary cube in contact
        with the front, bottom left corner of the cube
        :return: AssertionError if the setup fails, Nothing otherwise
        """
        s = {(1, 0, 0), (0, 1, 0), (0, 0, 1)}
        self.assertEqual(s, self.cube.get_neighbors(0, 0, 0))

    def test_get_neighbors_for_front_bottom_right_corner(self):
        """
        Checks for the right neighbors for an elementary cube in contact
        with the front, bottom right corner of the cube
        :return: AssertionError if the setup fails, Nothing otherwise
        """
        s = {(3, 0, 0), (4, 1, 0), (4, 0, 1)}
        self.assertEqual(s, self.cube.get_neighbors(4, 0, 0))

    def test_get_neighbors_for_back_top_left_corner(self):
        """
        Checks for the right neighbors for an elementary cube in contact
        with the back, top left corner of the cube
        :return: AssertionError if the setup fails, Nothing otherwise
        """
        s = {(3, 0, 0), (4, 1, 0), (4, 0, 1)}
        self.assertEqual(s, self.cube.get_neighbors(4, 0, 0))

    def test_get_neighbors_for_back_top_right_corner(self):
        """
        Checks for the right neighbors for an elementary cube in contact
        with the back, top right corner of the cube
        :return: AssertionError if the setup fails, Nothing otherwise
        """
        s = {(3, 4, 4), (4, 3, 4), (4, 4, 3)}
        self.assertEqual(s, self.cube.get_neighbors(4, 4, 4))

    def test_get_neighbors_for_back_bottom_left_corner(self):
        """
        Checks for the right neighbors for an elementary cube in contact
        with the back, bottom left corner of the cube
        :return: AssertionError if the setup fails, Nothing otherwise
        """
        s = {(1, 0, 4), (0, 1, 4), (0, 0, 3)}
        self.assertEqual(s, self.cube.get_neighbors(0, 0, 4))

    def test_get_neighbors_for_back_bottom_right_corner(self):
        """
        Checks for the right neighbors for an elementary cube in contact
        with the back, bottom right corner of the cube
        :return: AssertionError if the setup fails, Nothing otherwise
        """
        s = {(3, 0, 4), (4, 1, 4), (4, 0, 3)}
        self.assertEqual(s, self.cube.get_neighbors(4, 0, 4))


if __name__ == '__main__':
    unittest.main()

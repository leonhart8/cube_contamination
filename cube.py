"""
Module containing the cube class
"""


class Cube:
    """
    A cube is a 3D grid of elementary cubes. That is to say a cube of size n contains n^3
    elementary cubes.
    A cube can be seen as having an x-axis, a y-axis and a z-axis with a set of coordinates
    with respect to these axes in order to position elementary cubes
    """

    def __init__(self, size):
        """
        Constructor of the cube class, a 3D grid of n^3 elementary cubes
        :param size: int, the dimension of the grid in height, width and length
        :return: None, constructor
        """
        pass

    def get_neighbors_for_cube(self, coord_x, coord_y, coord_z):
        """
        Gets the set of neighbors of a given elementary cube in the grid
        :param coord_x: int, the coordinate on the x axis of a given cube
        :param coord_y: int, the coordinate on the y axis of a given cube
        :param coord_z: int, the coordinate on the z axis of a given cube
        :return:
        """
        pass

"""
Module containing the cube class
"""
import elementary_cube as ec
import numpy as np


class Cube:
    """
    A cube is a 3D grid of elementary cubes. That is to say a cube of size n contains n^3
    elementary cubes.

    A cube can be seen as having an x-axis, a y-axis and a z-axis with a set of coordinates
    with respect to these axes in order to position elementary cubes.

    An elementary cube is contaminated if its value is one, zero otherwise
    """

    def __init__(self, size):
        """
        Constructor of the cube class, a 3D grid of n^3 elementary cubes
        :param size: int, the dimension of the grid in height, width and length
        :return: None, constructor
        """
        self.cubes = np.zeros(size*size*size).reshape((size, size, size))
        self.size = size

    def get_size(self):
        """
        Getter for the cube's size
        :return: int, size of the cube
        """
        return self.size

    def get_cubes(self):
        """
        Getter for the cube's grid of cubes
        :return: a numpy array, this cube's cubes'
        """
        return self.cubes

    def get_neighbors(self, coord_x, coord_y, coord_z):
        """
        Gets the set of neighbors of a given elementary cube in the grid
        :param coord_x: int, the coordinate on the x axis of a given cube
        :param coord_y: int, the coordinate on the y axis of a given cube
        :param coord_z: int, the coordinate on the z axis of a given cube
        :return: set of tuples coordinates of the selected cube's neighbors
        """
        neighbors = set()
        size = self.get_size()
        if coord_x - 1 >= 0:
            neighbors.add((coord_x - 1, coord_y, coord_z))
        if coord_x + 1 < size:
            neighbors.add((coord_x + 1, coord_y, coord_z))
        if coord_y - 1 >= 0:
            neighbors.add((coord_x, coord_y - 1, coord_z))
        if coord_y + 1 < size:
            neighbors.add((coord_x, coord_y + 1, coord_z))
        if coord_z - 1 > 0:
            neighbors.add((coord_x, coord_y, coord_z - 1))
        if coord_z + 1 < size:
            neighbors.add((coord_x, coord_y, coord_z + 1))
        return neighbors

    def infection_rate(self):
        """
        Gives the cube's current infection rate
        :return: float, the cube's current infection rate
        """
        return np.sum(self.get_cubes()) / self.get_cubes().size

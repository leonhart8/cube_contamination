"""
Module which defines the Virus class, a simulation of a virus contamining cubes
"""
import numpy.random as npr

class Virus:
    """
    A Virus is defined for a given cube. It contaminates a single random cube for starters, then
    spreads by infecting all neighbors of a cube at a given time.

    At each time step the virus computes the next cubes to contaminate and proceeds to contaminate them.
    """

    def __init__(self, cube):
        """
        Constructor of the virus class. Takes only a cube and also initialize an empty
        set of coordinates of cubes to contaminate and an integer time step
        :param cube: the cube to infect
        """
        self.cube = cube
        self.next_contaminated = set()
        self.time_step = 0

    def get_cube(self):
        """
        Getter of the cube of this virus
        :return: Cube object
        """
        return self.cube

    def get_next_contaminated(self):
        """
        Getter of the next cubes to contaminate
        :return: set of coordinates of cubes to contaminate
        """
        return self.next_contaminated





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

    def get_time_step(self):
        """
        Getter of the current time step of the infection
        :return: get the current time step of the infection
        """
        return self.time_step

    def increment_time_step(self):
        """
        Increments the current time step
        :return: None, increments the current time step of the virus
        """
        self.time_step += 1

    def set_next_contaminated(self, next_contaminated):
        """
        Setter of the next cubes to contaminate
        :param next_contaminated: set of coordinates of the next cubes to contaminate
        :return: None, set of cubes to contaminate
        """
        self.next_contaminated = next_contaminated

    def find_next_to_contaminate(self):
        """
        Function which finds the set of coordinates of cubes to contaminate
        in the next step of the virus's infection
        :return: None, sets the set of coordinates of cubes to contaminate in the next_contaminated field
        """
        next_to_contaminate = set()
        cubes = self.get_cube().get_cubes()
        if self.get_time_step() == 0:
            next_to_contaminate.add(tuple([npr.randint(self.cube.get_size()) for _ in range(3)]))
        else:
            previously_contaminated = self.get_next_contaminated()
            for x, y, z in previously_contaminated:
                neighbors = self.cube.get_neighbors(x, y, z)
                for neighbor in neighbors:
                    i, j, k = neighbor
                    if cubes[i, j, k] == 0:
                        next_to_contaminate.add(neighbor)
        self.set_next_contaminated(next_to_contaminate)

    def infect(self):
        """
        Function which infects the cubes to contaminate.
        :return: None, sets the cubes of coordinates 'next_contaminated' to 1 to indicate contamination.
        Also increments the time step of the virus
        """
        next_contaminated = self.get_next_contaminated()
        grid = self.get_cube().get_cubes()
        for x, y, z in next_contaminated:
            grid[x, y, z] = 1
        self.increment_time_step()





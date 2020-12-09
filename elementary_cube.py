"""
Module containing the ElementaryCube class
"""


class ElementaryCube:
    """
    ElementaryCube class. ElementaryCubes are elementary parts of a larger cube.
    One ElementaryCube can be seen as a regular cube of size 1x1
    """

    def __init__(self):
        """
        Constructor of an elementary cube takes no arguments
        :return: None, sets the contamination state to False
        """
        pass

    def get_contamination_state(self):
        """
        Gets this elementary cube's contamination state
        :return: Bool, get the current contamination state
        """
        pass

    def contaminate(self):
        """
        Contaminates this ElementaryCube object
        :return: None, sets the contamination state to True
        """
        pass

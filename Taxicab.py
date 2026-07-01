# Author: Ayush Rajbhandari
# GitHub username: AyushRajbhandari
# Date: 6-30-26
# Description: Defines a Taxicab class that tracks current x and y coordinates,
#              along with an odometer reading that says the total distance traveled.

class Taxicab:
    """
    A class representing a taxicab that keeps track of its current
    x and y coordinates, as well as an odometer reading for total distance traveled.
    """

    def __init__(self, x_coord, y_coord):
        """
        Initializes a Taxicab object with the given x and y coordinates.
        The odometer starts at 0
        """
        self._x_coord = x_coord
        self._y_coord = y_coord
        self._odometer = 0

    def get_x_coord(self):
        """ Returns the current x-coordinate of the Taxicab."""
        return self._x_coord

    def get_y_coord(self):
        """ Returns the current y-coordinate of the Taxicab."""
        return self._y_coord

    def get_odometer(self):
        """ Returns the current odometer of Taxicab."""
        return self._odometer

    def move_x(self, distance):
        """
        Updates the x-coordinate and adds the absolute value of the
        Distance to the odometer.
        """
        self._x_coord += distance
        self._odometer += abs(distance)

    def move_y(self, distance):
        """
        Updates the y-coordinate and adds the absolute value of the
        Distance to the odometer.
        """
        self._y_coord += distance
        self._odometer += abs(distance)
      

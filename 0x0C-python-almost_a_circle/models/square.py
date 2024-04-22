#!/usr/bin/python3
"""
Defines a Square class.
"""
from models.rectangle import Rectangle


class Square(Rectangle):
    """
    Represents a square.
    """

    def __init__(self, size, x=0, y=0, id=None):
        """
        Initializes a new Square.
        """
        super().__init__(size, size, x, y, id)

    @property
    def size(self):
        """Get/set the size of the Square."""
        return self.width

    @size.setter
    def size(self, value):
        self.width = value
        self.height = value

    def update(self, *args, **kwargs):
        """
        Updates the Square.
        """
        if args:
            attrs = ["id", "size", "x", "y"]
            for idx, arg in enumerate(args):
                setattr(self, attrs[idx], arg)
        elif kwargs:
            for key, value in kwargs.items():
                setattr(self, key, value)

    def to_dictionary(self):
        """Returns the dictionary representation of the Square."""
        square_dict = {
            "id": self.id,
            "size": self.width,
            "x": self.x,
            "y": self.y
        }
        return square_dict

    def __str__(self):
        """Returns the print() and str() representation of a Square."""
        return "[Square] ({}) {}/{} - {}".format(self.id, self.x, self.y,
                                                 self.width)


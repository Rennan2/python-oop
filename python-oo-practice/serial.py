"""Python serial number generator."""

from typing import Any


class SerialGenerator:
    """Machine to create unique incrementing serial numbers.
    
    >>> serial = SerialGenerator(start=100)

    >>> serial.generate()
    100

    >>> serial.generate()
    101

    >>> serial.generate()
    102

    >>> serial.reset()

    >>> serial.generate()
    100
    """
    def __init__(self, start=0):
        """New generator, starting at start"""
        self.start = self.current = self.next = start

    def __repr__(self):
        """Show represention"""
        return f"<SerialGenerator start={self.start} next={self.next}>"
    
    def generate(self):
        """ Return serial"""
        self.current += 1 
        self.next = self.current + 1
        return self.current
    
    def reset (self):
        self.next = self.current = self.start
        return self.start


"""Module for defining a Rat class in the petting zoo scurrying section."""

# import the python datetime module to help us create a timestamp
from datetime import date


# Define the Rat class
class Rat:
    """A class representing a rat in the petting zoo."""

    def __init__(self, name, species):
        # Define the properties of animal
        self.name = name
        self.species = species
        self.date_added = date.today()
        self.scurrying = True

    def __str__(self):
        return f"{self.name} is a {self.species}"

"""Module for defining a Frog class in the petting zoo jumping section."""

# import the python datetime module to help us create a timestamp
from datetime import date


# Define the Frog class
class Frog:
    """A class representing a frog in the petting zoo."""

    def __init__(self, name, species):
        # Define the properties of animal
        self.name = name
        self.species = species
        self.date_added = date.today()
        self.jumping = True

    def __str__(self):
        return f"{self.name} is a {self.species}"

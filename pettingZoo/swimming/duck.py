"""Module for defining a Duck class in the petting zoo swimming section."""

# import the python datetime module to help us create a timestamp
from datetime import date


# Define the Duck class
class Duck:
    """A class representing a duck in the petting zoo."""

    def __init__(self, name, species):
        # Define the properties of animal
        self.name = name
        self.species = species
        self.date_added = date.today()
        self.swimming = True

    def __str__(self):
        return f"{self.name} is a {self.species}"

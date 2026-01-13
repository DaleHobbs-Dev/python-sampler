"""Module for defining a Turtle class in the petting zoo crawling section."""

# import the python datetime module to help us create a timestamp
from datetime import date


# Define the Turtle class
class Turtle:
    """A class representing a turtle in the petting zoo."""

    def __init__(self, name, species):
        # Define the properties of animal
        self.name = name
        self.species = species
        self.date_added = date.today()
        self.crawling = True

    def __str__(self):
        return f"{self.name} is a {self.species}"

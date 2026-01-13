"""Module for defining a Turtle class in the petting zoo crawling section."""

# import the python datetime module to help us create a timestamp
from datetime import date


# Define the Snake class
class Snake:
    """A class representing a snake in the petting zoo."""

    def __init__(self, name, species):
        # Define the properties of animal
        self.name = name
        self.species = species
        self.date_added = date.today()
        self.slithering = True

    def __str__(self):
        return f"{self.name} is a {self.species}"

"""Module for defining a Goat class in the petting zoo walking section."""

# import the python datetime module to help us create a timestamp
from datetime import date


# Define the Goat class
class Goat:
    """A class representing a goat in the petting zoo."""

    def __init__(self, name, shift, species):
        allowed_shifts = {"morning", "midday", "afternoon"}

        normalized_shift = shift.strip().lower()

        if normalized_shift not in allowed_shifts:
            raise ValueError(f"shift must be one of {allowed_shifts}, got '{shift}'")

        # Define the properties of animal
        self.name = name
        self.species = species
        self.shift = normalized_shift
        self.date_added = date.today()
        self.walking = True

    def __str__(self):
        return f"{self.name} is a {self.species}"

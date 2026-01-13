"""Module for defining a Llama class in the petting zoo walking section."""

# import the python datetime module to help us create a timestamp
from datetime import date


# Define the Llama class
class Llama:
    """A class representing a llama in the petting zoo."""

    def __init__(self, name, shift, species, food):
        allowed_shifts = {"morning", "midday", "afternoon"}

        normalized_shift = shift.strip().lower()

        if normalized_shift not in allowed_shifts:
            raise ValueError(f"shift must be one of {allowed_shifts}, got '{shift}'")

        # Establish the properties of a Llama
        self.name = name
        self.shift = normalized_shift
        self.species = species
        self.date_added = date.today()
        self.walking = True
        self.food = food

    def feed(self):
        """Method to feed the llama and print a feeding message with a timestamp."""
        print(f'{self.name} was fed {self.food} on {date.today().strftime("%m/%d/%Y")}')

    def __str__(self):
        return f"{self.name} is a {self.species}"

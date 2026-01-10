# Define the Seal class
class Seal:
    """A class representing a seal in the petting zoo."""

    def __init__(self, name, species):
        # Define the properties of animal
        self.name = name
        self.species = species
        self.date_added = date.today()
        self.swimming = True

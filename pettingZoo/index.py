"""Module defining the animal classes for the petting zoo."""

# import the python datetime module to help us create a timestamp
from datetime import date


# Define the Llama class
class Llama:
    """A class representing a llama in the petting zoo."""

    def __init__(self, name, species):
        # Establish the properties of each animal
        # with a default value
        self.name = name
        self.species = species
        self.date_added = date.today()
        self.walking = True


# Define the Donkey class
class Donkey:
    """A class representing a donkey in the petting zoo."""

    def __init__(self, name, species):
        # Define the properties of animal
        self.name = name
        self.species = species
        self.date_added = date.today()
        self.walking = True


# Define the Goat class
class Goat:
    """A class representing a goat in the petting zoo."""

    def __init__(self, name, species):
        # Define the properties of animal
        self.name = name
        self.species = species
        self.date_added = date.today()
        self.walking = True


# Define the Deer class
class Deer:
    """A class representing a deer in the petting zoo."""

    def __init__(self, name, species):
        # Define the properties of animal
        self.name = name
        self.species = species
        self.date_added = date.today()
        self.walking = True


# Define the Cow class
class Cow:
    """A class representing a cow in the petting zoo."""

    def __init__(self, name, species):
        # Define the properties of animal
        self.name = name
        self.species = species
        self.date_added = date.today()
        self.walking = True


# Define the Snake class
class Snake:
    """A class representing a snake in the petting zoo."""

    def __init__(self, name, species):
        # Define the properties of animal
        self.name = name
        self.species = species
        self.date_added = date.today()
        self.slithering = True


# Define the Spider class
class Spider:
    """A class representing a spider in the petting zoo."""

    def __init__(self, name, species):
        # Define the properties of animal
        self.name = name
        self.species = species
        self.date_added = date.today()
        self.crawling = True


# Define the Turtle class
class Turtle:
    """A class representing a turtle in the petting zoo."""

    def __init__(self, name, species):
        # Define the properties of animal
        self.name = name
        self.species = species
        self.date_added = date.today()
        self.crawling = True


# Define the Frog class
class Frog:
    """A class representing a frog in the petting zoo."""

    def __init__(self, name, species):
        # Define the properties of animal
        self.name = name
        self.species = species
        self.date_added = date.today()
        self.jumping = True


# Define the Rat class
class Rat:
    """A class representing a rat in the petting zoo."""

    def __init__(self, name, species):
        # Define the properties of animal
        self.name = name
        self.species = species
        self.date_added = date.today()
        self.scurrying = True


# Define the Fish class
class Fish:
    """A class representing a fish in the petting zoo."""

    def __init__(self, name, species):
        # Define the properties of animal
        self.name = name
        self.species = species
        self.date_added = date.today()
        self.swimming = True


# Define the Eel class
class Eel:
    """A class representing an eel in the petting zoo."""

    def __init__(self, name, species):
        # Define the properties of animal
        self.name = name
        self.species = species
        self.date_added = date.today()
        self.swimming = True


# Define the Penguin class
class Penguin:
    """A class representing a penguin in the petting zoo."""

    def __init__(self, name, species):
        # Define the properties of animal
        self.name = name
        self.species = species
        self.date_added = date.today()
        self.swimming = True


# Define the Duck class
class Duck:
    """A class representing a duck in the petting zoo."""

    def __init__(self, name, species):
        # Define the properties of animal
        self.name = name
        self.species = species
        self.date_added = date.today()
        self.swimming = True


# Example of creating an instance of Llama
miss_fuzz = Llama("Miss Fuzz", "domestic llama")

# Example of creating an instance of Donkey
mr_stubborn = Donkey("Mr. Stubborn", "domestic donkey")

# Example of creating an instance of Goat
billy_the_kid = Goat("Billy the Kid", "domestic goat")

# Example of creating an instance of Deer
bambi = Deer("Bambi", "white-tailed deer")

# Example of creating an instance of Cow
daisy = Cow("Daisy", "domestic cow")

# Example of creating an instance of Snake
slitherin = Snake("Slitherin", "corn snake")

# Example of creating an instance of Spider
webster = Spider("Webster", "tarantula")

# Example of creating an instance of Turtle
shelly = Turtle("Shelly", "red-eared slider")

# Example of creating an instance of Frog
hoppy = Frog("Hoppy", "tree frog")

# Example of creating an instance of Rat
squeaky = Rat("Squeaky", "domestic rat")

# Example of creating an instance of Fish
bubbles = Fish("Bubbles", "goldfish")

# Example of creating an instance of Eel
slimy = Eel("Slimy", "freshwater eel")

# Example of creating an instance of Penguin
tux = Penguin("Tux", "emperror penguin")

# Example of creating an instance of Duck
quacky = Duck("Quacky", "mallard duck")

# Example of creating an instance of Seal
flippers = Seal("Flippers", "harbor seal")

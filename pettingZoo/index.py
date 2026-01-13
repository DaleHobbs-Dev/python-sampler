"""Module defining the animal classes for the petting zoo."""

# Importing animal classes from their respective modules
from swimming import Fish, Eel, Duck, Penguin, Seal
from slithering import Snake
from crawling import Spider, Turtle
from jumping import Frog
from scurrying import Rat
from walking import Llama, Donkey, Goat, Deer, Cow

# Example of creating an instance of Llama
miss_fuzz = Llama(
    name="Miss Fuzz", shift="Morning", species="domestic llama", food="Llama Chow"
)
miss_fuzz.feed()

# Another Llama
roberto = Llama(
    name="Roberto", shift="midday", species="alpaca llama", food="Llama Premium"
)
print(
    f"{roberto.name} the {roberto.species} is available to pet during the {roberto.shift} shift."
)
print(roberto)

# Example of creating an instance of Donkey
mr_stubborn = Donkey(name="Mr. Stubborn", shift="morning", species="domestic donkey")

# Example of creating an instance of Goat
billy_the_kid = Goat(name="Billy the Kid", shift="Afternoon", species="domestic goat")

# Example of creating an instance of Deer
bambi = Deer(name="Bambi", shift="midday", species="white-tailed deer")

# Example of creating an instance of Cow
daisy = Cow(name="Daisy", shift="Afternoon", species="domestic cow")

# Example of creating an instance of Snake
slitherin = Snake(name="Slitherin", species="corn snake")

# Example of creating an instance of Spider
webster = Spider(name="Webster", species="tarantula")

# Example of creating an instance of Turtle
shelly = Turtle(name="Shelly", species="red-eared slider")

# Example of creating an instance of Frog
hoppy = Frog(name="Hoppy", species="tree frog")

# Example of creating an instance of Rat
squeaky = Rat(name="Squeaky", species="domestic rat")

# Example of creating an instance of Fish
bubbles = Fish(name="Bubbles", species="goldfish")

# Example of creating an instance of Eel
slimy = Eel(name="Slimy", species="freshwater eel")

# Example of creating an instance of Penguin
tux = Penguin(name="Tux", species="emperror penguin")

# Example of creating an instance of Duck
quacky = Duck(name="Quacky", species="mallard duck")

# Example of creating an instance of Seal
flippers = Seal(name="Flippers", species="harbor seal")

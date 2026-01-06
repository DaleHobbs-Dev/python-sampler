planet_list = ["Mercury", "Mars"]

planet_list.append("Jupiter")

planet_list.append("Saturn")

last_planets = ["Uranus", "Neptune"]

planet_list.extend(last_planets)

planet_list.insert(1, "Venus")

planet_list.insert(2, "Earth")

planet_list.append("Pluto")

rocky_planets = planet_list[0:4]

del planet_list[8]

print("All Planets:")
for planet in planet_list:
    print(planet)

print("\nRocky Planets:")
for rocky in rocky_planets:
    print(rocky)

# Spacecraft and the Planets They Visited as tuples inside a list
spacecrafts = [
    ("Mariner 10", "Mercury"),
    ("MESSENGER", "Mercury"),
    ("Viking 1", "Mars"),
    ("Viking 2", "Mars"),
    ("Pioneer 10", "Jupiter"),
    ("Pioneer 11", "Jupiter"),
    ("Voyager 1", "Saturn"),
    ("Voyager 2", "Saturn"),
    ("Voyager 2", "Uranus"),
    ("Voyager 2", "Neptune"),
    ("Voyager 1", "Jupiter"),
    ("Voyager 2", "Jupiter"),
    ("New Horizons", "Pluto"),
    ("Juno", "Jupiter"),
    ("Galileo", "Jupiter"),
    ("Cassini", "Saturn"),
    ("Curiosity", "Mars"),
    ("Perseverance", "Mars"),
    ("Spirit", "Mars"),
    ("Opportunity", "Mars"),
    ("Pathfinder", "Mars"),
    ("InSight", "Mars"),
    ("Zhurong", "Mars"),
    ("Cassini-Huygens", "Saturn"),
    ("Viking Orbiter", "Mars"),
    ("Cassini", "Jupiter"),
    ("New Horizons", "Jupiter"),
    ("Ulysses", "Jupiter"),
    ("Dawn", "Mars"),
    ("Phoenix", "Mars"),
    ("Odyssey", "Mars"),
    ("Mariner 9", "Mars"),
    ("Mariner 4", "Mars"),
    ("Mariner 6", "Mars"),
    ("Mariner 7", "Mars"),
    ("Venera 7", "Venus"),
    ("Venera 9", "Venus"),
    ("Magellan", "Venus"),
    ("Galileo", "Venus"),
    ("Vega 1", "Venus"),
    ("Vega 2", "Venus"),
    ("Pioneer Venus 1", "Venus"),
    ("Pioneer Venus 2", "Venus"),
    ("Mariner 2", "Venus"),
    ("Mariner 5", "Venus"),
    ("Mariner 10", "Venus"),
    ("Venus Express", "Venus"),
    ("Akatsuki", "Venus"),
    ("Helios 1", "Mercury"),
    ("Helios 2", "Mercury"),
    ("MESSENGER", "Venus"),
    ("Venera 1", "Venus"),
    ("Venera 2", "Venus"),
    ("Venera 3", "Venus"),
    ("Venera 4", "Venus"),
    ("Venera 5", "Venus"),
    ("Venera 6", "Venus"),
    ("Venera 8", "Venus"),
    ("Venera 10", "Venus"),
    ("Venera 11", "Venus"),
    ("Venera 12", "Venus"),
    ("Venera 13", "Venus"),
    ("Venera 14", "Venus"),
]

# Displaying spacecrafts and the planets they visited
print("\nSpacecrafts and the Planets They Visited:")
for craft, planet in spacecrafts:
    print(f"{craft} has visited")
    print("--------------------------------")
    print(f"{planet}\n")


# Displaying planets with their spacecraft visitors
print("Planets with their Spacecraft Visitors:")

for planet in planet_list:
    print(f"\n{planet} has been visited by:")
    found_any = False  # track whether we printed at least one craft

    for craft, visited_planet in spacecrafts:
        if visited_planet == planet:
            print(f"- {craft}")
            found_any = True

    if not found_any:
        print("No spacecraft have visited this planet yet.")

    print("--------------------------------")

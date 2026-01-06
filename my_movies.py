# Initialize an empty list to store favorite movies
favorite_movies = []


# Function to add a movie and print that it was added
def add_movie(movie):
    favorite_movies.append(movie)
    print(f"Movie '{movie}' added to favorites.")


# Function to remove a movie and print that it was removed. If the movie is not found, print a message indicating so.
def remove_movie(movie):
    if movie in favorite_movies:
        favorite_movies.remove(movie)
        print(f"Movie '{movie}' removed from favorites.")
    else:
        print(f"Movie '{movie}' not found in favorites.")


# Function to display all favorite movies. If favorite_movies is empty, print a message indicating that there are no favorite movies.
def display_movies():
    if not favorite_movies:
        print("You have no favorite movies.")
    else:
        print("Favorite Movies:")
        for movie in favorite_movies:
            print(f"- {movie}")


# Function that counts the number of favorite movies and prints the count
def count_movies():
    count = len(favorite_movies)
    print(f"You have {count} favorite movie(s).")


# Function that checks if a movie is in the favorite movies list and prints an appropriate message
def is_favorite(movie):
    if movie in favorite_movies:
        print(f"'{movie}' is in your favorite movies.")
    else:
        print(f"'{movie}' is not in your favorite movies.")


# Function that clears the favorite movies list. It will check if you want to clear the list with a "yes" confirmation, then upon confirmation, it will clear the list and print a message indicating that the list has been cleared.
def clear_movies():
    confirmation = input(
        "Are you sure you want to clear your favorite movies list? Type 'y' to confirm: "
    )
    if confirmation.lower() == "y":
        favorite_movies.clear()
        print("Favorite movies list has been cleared.")
    else:
        print("Clear operation cancelled.")


# Adding movies
add_movie("Inception")
add_movie("The Matrix")
add_movie("Interstellar")

# Displaying movies
display_movies()

# Counting movies
count_movies()

# Checking if a movie is a favorite
is_favorite("The Matrix")
is_favorite("Avatar")

# Removing a movie
remove_movie("Inception")

# Clearing the movies list
clear_movies()

# Displaying movies again
display_movies()

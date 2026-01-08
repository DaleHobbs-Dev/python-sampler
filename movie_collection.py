"""Movie Collection Management System"""

# List to store movie information
movie_collection = [
    ("The Shawshank Redemption", "Frank Darabont", 1994),
    ("The Godfather", "Francis Ford Coppola", 1972),
    ("The Dark Knight", "Christopher Nolan", 2008),
    ("Pulp Fiction", "Quentin Tarantino", 1994),
]


# Function to display all movies in the collection
def display_movies():
    """Displays all movies in the movie collection."""
    print("Movie Collection:")
    for movie_title, movie_director, year_released in movie_collection:
        print(
            f"Title: {movie_title}, Director: {movie_director}, Year: {year_released}"
        )


# Function to add a new movie to the collection
def add_movie(movie_title, movie_director, year_released):
    """Adds a new movie to the movie collection."""
    new_movie = (movie_title, movie_director, year_released)
    movie_collection.append(new_movie)
    print(
        f"Movie '{movie_title}' directed by {movie_director} added to the collection."
    )


# Function to search for movies by a director
def search_by_director(movie_director):
    """Searches for movies by the given director."""
    movies_by_director = []
    for movie in movie_collection:
        _, current_director, _ = movie
        if current_director.lower() == movie_director.lower():
            movies_by_director.append(movie)
    return movies_by_director


# Remove a movie from the collection
def remove_movie(movie_title):
    """Removes a movie from the movie collection by title."""
    for movie in movie_collection[:]:
        movie_title_in_list, _, _ = movie
        if movie_title_in_list.lower() == movie_title.lower():
            movie_collection.remove(movie)
            print(f"Movie '{movie_title}' removed from the collection.")
            return

    print(f"Movie '{movie_title}' not found in the collection.")


# Displaying the movies
display_movies()

# Adding a new movie
add_movie("Inception", "Christopher Nolan", 2010)

# Displaying the movies again
display_movies()

# Searching for movies by Christopher Nolan
movies_by_nolan = search_by_director("Christopher Nolan")
print("Movies by Christopher Nolan:")
for title, director, year in movies_by_nolan:
    print(f"Title: {title}, Year: {year}")

# Removing a movie
remove_movie("Pulp Fiction")

# Removing a movie that does not exist
remove_movie("Avatar")

# Displaying the movies after removal
display_movies()

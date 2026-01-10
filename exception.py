"""Module demonstrating exception handling in Python."""


# Function to add two numbers with exception handling for TypeError
def add_numbers(a, b):
    """Adds two numbers and handles TypeError exceptions."""
    try:
        result = a + b
        print(f"The result is: {result}")
    except TypeError:
        print("Please provide two integers as arguments when invoking this function.")


# Example usage of add_numbers function where TypeError might occur
add_numbers(5, "10")

# Example dictionary for demonstration
my_dict = {"name": "Alice", "age": 30, "city": "New York"}


# Function to get value from dictionary with exception handling for TypeError
def get_value(dictionary, key):
    try:
        value = dictionary[key]
        print(f"The value for '{key}' is: {value}")
    except KeyError:
        print(f"The key '{key}' does not exist in the dictionary.")
    except TypeError:
        print("Please provide a valid dictionary and key.")


# Example usage
get_value(my_dict, "name")
get_value(my_dict, "occupation")

# Example usage of get_value function where TypeError might occur
shopping_cart_items = []


# Function to calculate average price of items in shopping cart
def average_price(cart_items):
    """Calculates the average price of items in the shopping cart."""
    average = 0

    for item in cart_items:
        average += item.price

    try:
        average = average / len(cart_items)
        return average
    except ZeroDivisionError:
        return 0


average_price_of_cart_items = average_price(shopping_cart_items)

print(f"Your average cart item price is {average_price_of_cart_items} dollars")

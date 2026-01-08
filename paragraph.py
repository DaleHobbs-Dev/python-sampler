"""Module to extract unique words from a paragraph and compare two paragraphs."""


# Function to extract unique words from a paragraph
def extract_unique_words(paragraph):
    """Extracts unique words from the given paragraph."""
    words = paragraph.lower().split()
    unique_words = set(words)
    return unique_words


# Function to find common words between two sets
def find_common_words(set1, set2):
    """Finds common words between two sets."""
    return set1.intersection(set2)


# Function to find words unique to the first set
def find_unique_words(set1, set2):
    """Finds words unique to the first set compared to the second set."""
    return set1.difference(set2)


# Function to display results
def display_results(common, unique1, unique2):
    """Displays the comparison results of common and unique words."""
    print("Comparison Results:")
    print("\nCommon Words:")
    for word in common:
        print(word)

    print("\nUnique Words in Paragraph 1:")
    for word in unique1:
        print(word)

    print("\nUnique Words in Paragraph 2:")
    for word in unique2:
        print(word)


# Example paragraphs
paragraph1 = "Python is a great programming language. Python is popular and powerful."
paragraph2 = "Python is widely used in data science. Data science is an exciting field."

# Extracting unique words from paragraphs
unique_words1 = extract_unique_words(paragraph1)
unique_words2 = extract_unique_words(paragraph2)

# Finding common and unique words
common_words = find_common_words(unique_words1, unique_words2)
unique_to_paragraph1 = find_unique_words(unique_words1, unique_words2)
unique_to_paragraph2 = find_unique_words(unique_words2, unique_words1)

# Displaying the comparison results
display_results(common_words, unique_to_paragraph1, unique_to_paragraph2)

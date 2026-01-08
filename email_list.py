"""Module to manage email subscribers and unsubscribers using sets."""

# Initialize empty sets
subscribers = set()
unsubscribers = set()


# Function to add an email
def add_email(email, set_name):
    """Adds an email to the specified set."""
    set_name.add(email)
    print(
        f"Email '{email}' added to {'subscribers' if set_name == subscribers else 'unsubscribers'}."
    )


# Function to remove an email
def remove_email(email, set_name):
    """Removes an email from the specified set."""
    try:
        set_name.remove(email)
        print(
            f"Email '{email}' removed from {'subscribers' if set_name == subscribers else 'unsubscribers'} list"
        )
    except KeyError:
        print(
            f"Email `{email}` not found in the {'subscribers' if set_name == subscribers else 'unsubscribers'} list"
        )


# Function to display emails
def display_emails(set_name):
    """Displays all emails in the specified set."""
    count = len(set_name)
    if set_name == subscribers:
        print(f"List of Subscribers ({count})\n-------------------")
    else:
        print(f"List of Unsubscribers ({count})\n--------------------")

    for email in set_name:
        print(f"* {email}")


# Function to find active subscribers who are not unsubscribed
def find_active_subscribers():
    """Finds and displays active subscribers who are not unsubscribed."""
    active_subscribers = subscribers.difference(unsubscribers)
    count = len(active_subscribers)
    print(f"Active Subscribers (not unsubscribed) ({count}):")
    for email in active_subscribers:
        print(f"* {email}")
    return active_subscribers


# Adding emails to subscribers (notice that some people subscribe more than once)
add_email("user1@example.com", subscribers)
add_email("user3@example.com", subscribers)
add_email("user4@example.com", subscribers)
add_email("user11@example.com", subscribers)
add_email("user5@example.com", subscribers)
add_email("user6@example.com", subscribers)
add_email("user2@example.com", subscribers)
add_email("user5@example.com", subscribers)
add_email("user2@example.com", subscribers)
add_email("user7@example.com", subscribers)
add_email("user8@example.com", subscribers)
add_email("user9@example.com", subscribers)
add_email("user2@example.com", subscribers)
add_email("user11@example.com", subscribers)
add_email("user7@example.com", subscribers)
add_email("user10@example.com", subscribers)
add_email("user12@example.com", subscribers)

# Adding emails to unsubscribers
add_email("user6@example.com", unsubscribers)
add_email("user8@example.com", unsubscribers)
add_email("user1@example.com", unsubscribers)
add_email("user10@example.com", unsubscribers)

# Removing an email from sets
remove_email("user3@example.com", subscribers)
remove_email("user3@example.com", unsubscribers)

# Displaying subscribers and unsubscribers
display_emails(subscribers)
display_emails(unsubscribers)

# Finding active subscribers
find_active_subscribers()

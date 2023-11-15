# Using def function for make_shirt(size="large", message="I love python")
def make_shirt(size="large", message="I love Python"):
    """Printing a sentence that summarises the size and message of a shirt."""
    print(f"I will make a shirt of {size}-sized with the message: '{message}'.")

# Making a large shirt with the "I love Python" message
make_shirt()

# Making a medium shirt with the "I love Python" message
make_shirt(size="medium")

# Making a shirt of any size with a different message
make_shirt(size="small", message="Happy Eid")

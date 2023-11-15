# Using def function for make_shirt(size, message)
def make_shirt(size, message):
    """Printing a sentence that summarises the size and message of a shirt."""
    print(f"I will make a shirt of {size}-sized with the message: '{message}'.")

# Using positional argumnets to call the fuction once
make_shirt("large", "Happy Eid")


# Using positional argumnets to call the fuction for the second time
make_shirt(size="small", message="Merry Christmas")
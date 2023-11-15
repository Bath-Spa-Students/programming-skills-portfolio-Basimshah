# Using def function for describe_city(city, country="Unknown")
def describe_city(city, country="Pakistan"):
    """Printing a simple sentence that describes the city and its country."""
    print(f"{city} is located in {country}.")

# Call the function for three different cities
describe_city("Gaza", "Palestine")
describe_city("Berlin", "Germnany")
describe_city("Islamabad")
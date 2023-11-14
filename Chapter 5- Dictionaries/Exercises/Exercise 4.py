# Create a dictionary of rivers and their respective countries
rivers = {
    'nile': 'Egypt',
    'Jhelum': 'Pakistan',
    'Volga': 'Russia'
}

# Print a sentence about each river
for river, country in rivers.items():
    print(f"The {river.title()} river flow through {country}.")

# Print the names of each river
print("\nRivers:")
for river in rivers.keys():
    print(river.title())

# Print the names of each country
print("\nCountries:")
for country in rivers.values():
    print(country)
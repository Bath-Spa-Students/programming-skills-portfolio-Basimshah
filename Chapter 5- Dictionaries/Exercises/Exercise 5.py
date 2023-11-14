# Storing Animal kind and their owner's name in dictionaries
pet_1 = {'kind': 'Cat', 'owner': 'Basim'}
pet_2 = {'kind': 'Parrot', 'owner': 'Maryam'}
pet_3 = {'kind': 'Rabbit', 'owner': 'Yumna'}
pet_4 = {'kind': 'Dog', 'owner': 'Hamza'}
pet_5 = {'kind': 'Hamster', 'owner': 'Fahad'}


# Creating a list with all the dictionaries
pets = [pet_1, pet_2, pet_3, pet_4, pet_5]

# Looping through the list and printing information of each pet
for pet in pets:
    print(f"\nPet's Kind: {pet['kind']}")
    print(f"Pet's Owner: {pet['owner']}")

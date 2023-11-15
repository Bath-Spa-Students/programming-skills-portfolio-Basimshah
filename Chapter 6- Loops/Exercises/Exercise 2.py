# Utilizing a while loop to inquire about the user's age in order to ascertain the ticket price.
while True:
    # Requesting the user to enter their age and type 'quit' when they have completed the input.
    person_age = input("Please enter your age for the ticket price and type 'quit' once you're done: ")

    # Verifying whether the user entered 'quit'; if so, break the loop.
    if person_age.lower() == 'quit':
        break

    # Transforming the entered age into an integer for the purpose of comparison.
    person_age = int(person_age)

    # printing the cost of the ticket by determining the movie ticket price based on the individual's age.
    if person_age < 3:
        print("Your movie ticket is free.")
    elif 3 <= person_age <= 12:
        print("Your movie ticket price is $10.")
    else:
        print("Your movie ticket price is $15.")

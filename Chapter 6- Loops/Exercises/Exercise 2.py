# Using while loop to ask the user for their age to determine the ticket price
while True:
    # Asking the user to input their age and type 'quit' once they are finished
    person_age = input("Please enter your age for the ticket price and type 'quit' once you're done: ")

    # Checking if the user entered 'quit'; if true, break the loop
    if person_age.lower() == 'quit':
        break

    # Convert the entered age to an integer for comparison
    person_age = int(person_age)

    # printing the coast of the ticket by determine the movie ticket price based on the person's age
    if person_age < 3:
        print("Your movie ticket is free.")
    elif 3 <= person_age <= 12:
        print("Your movie ticket price is $10.")
    else:
        print("Your movie ticket price is $15.")

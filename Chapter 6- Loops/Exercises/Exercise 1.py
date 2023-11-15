# Using while loop to ask the user for pizza toppings
while True:
    # Asking the user to input the desired pizza topping and type 'quit' once they are finished
    pizza_topping = input("Please input the pizza topping you desire and type 'quit' once you are done: ")
    
    # Checking if the user entered 'quit'; if true, break the loop
    if pizza_topping.lower() == "quit":
        break
    
    # Printing the pizza topping that will be added
    print(f"{pizza_topping} will be added to your pizza as toppings.")

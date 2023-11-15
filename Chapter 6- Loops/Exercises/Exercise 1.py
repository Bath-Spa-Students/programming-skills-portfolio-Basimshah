while True:
    pizza_topping = input("Please input the pizza topping you desire and type 'quit' once you are done: ")
    
    if pizza_topping.lower() == "quit":
        break
    
    print(f"You'll add {pizza_topping} to your pizza.")

# Assigning values to a list "sandwich_orders"
sandwich_orders = ["Tripleta", "panelle", "tuna", "mitraillette", "cemita"]

# Making an empty list "finished_sandwiches"
finished_sandwiches = []

# using while Loop through the list of sandwich orders
while sandwich_orders:
    current_order = sandwich_orders.pop(0)  # Take the first sandwich order
    print(f"I have prepared your {current_order} sandwich.")
    finished_sandwiches.append(current_order)  # Move the finished sandwich to the list

# Printing a message showing each sandwich that was prepared
print("\nList of finished sandwiches:")
for sandwich in finished_sandwiches:
    print(sandwich.title())

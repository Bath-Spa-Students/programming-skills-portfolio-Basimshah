# initialized a list that contains the names of the guests invited for the dinner
guests = ["Ahad Pervaize", "Huzaifa awan", "Ahrar Abid"]

# Print a message saying that you can invite only two people for dinner
print("I can only invite two people for dinner.")

# Use pop() to remove guests from your list and apologize for not inviting them
while len(guests) > 2:
    removed_guest = guests.pop()
    print(f"Sorry, {removed_guest}, I can't invite you to dinner this time.")

# Print a message to both who are still on your list, letting them know they're still invited
for guest in guests:
    print(f"Dear {guest}, you are still invited to dinner.")

# Using del to remove the remaining names from your list, leaving an empty list
del guests[:]

# Print your list to make sure that your list is empty
print("My guest list is now empty:", guests)
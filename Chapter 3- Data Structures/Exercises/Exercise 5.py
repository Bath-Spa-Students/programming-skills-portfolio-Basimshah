# initialized a list that contains the names of the guests invited for the dinner
guests = ["Ahad Pervaize", "Huzaifa awan", "Moosa Kamran"]

# declaring a variable that contains the name of the guest that couldn't make it to the dinner
guest_cant_make_it = "Moosa Kamran"
# printing the guest
print(f"Unfortunately, {guest_cant_make_it} can't make it to dinner.")

# Replace the guest who can't make it with the new person you are inviting uisng a new variable
new_guest = "Ahrar Abid"
guests.remove(guest_cant_make_it)
guests.append(new_guest)

# used for loop to iterate through the modified list and print a common message for each guest with their names
for guest in guests:
    print(f"Dear {guest}, you are invited to dinner. Please join us for a special evening!")

#initializing a list
locations =['dubai','paris', 'switzerland', 'london', 'amsterdam', 'new York']

#printing the list
print("printing the original list\n", locations)


#printing a copy of list in alphabetical order using the sorted() funtion
print("\n\nsorting a copy of original list in alphabetical order\n", sorted(locations))

#printing the original list to show the original order hasn't be altered
print("\n\nprinting the original list\n", locations)

#printing a copy of list in reverse alphabetical order using the reverse attribute of the sorted() funtion
print("\n\nsorting a copy of original list in reverse alphabetical order\n", sorted(locations, reverse=True))

#printing the original list to show the original order hasn't be altered
print("\n\nprinting the original list\n", locations)

#reversing the order of the list using the reverse() function
locations.reverse()
print("\n\nreversing the order of the list\n", locations)

#reversing the order of the list back to original using the reverse() function
locations.reverse()
print("\n\nreversing the order of the list back to original\n", locations)

#sorting the original list in alphabetical order
locations.sort()
#printing the sorted list
print("\n\nsorting a the list in alphabetical order\n", locations)

#printing the list in reverse alphabetical order using the reverse attribute of the sort() function
locations.sort(reverse=True)
#printing the sorted list
print("\n\nsorting the list in reverse alphabetical order\n", locations, "\n")
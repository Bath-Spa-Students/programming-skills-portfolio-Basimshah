#Assigning a value "17" to the variable "age".
age = int(input("Enter age "))

#Using if-elif-else chain to match the age and proceed.
if age < 2:
    print("You are a baby.")
elif age < 4:
    print("You are a toddler.")
elif age < 13:
    print("You are a kid.")
elif age < 20:
    print("You are a teenager.")
elif age < 65:
    print("You are an adult.")
else:
    print("You are an elder.")

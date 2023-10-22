# Assigning the value to variable "cost_of_usbstick" and "budget_of_girl"
cost_of_usbstick = 6
budget_of_girl = 50

# Dividing the variables "cost_of_usbstick" and "budget_of_girl" to get the variable "usbsticks_bought"
usbsticks_bought = budget_of_girl // cost_of_usbstick

# subtracting the product of variable  "cost_of_usbstick" and "usbsticks_bought" from "budget_remaining"
budget_remaining = budget_of_girl - (cost_of_usbstick*usbsticks_bought)

# pinting the total usb sticks bought and the budget remaining
print(f"She can buy a total of {usbsticks_bought} USB sticks with £{budget_remaining} left.")
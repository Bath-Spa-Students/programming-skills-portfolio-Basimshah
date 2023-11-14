#Assigning a value to each variable stored in dictionary "glossary"
glossary = {
    "string": "A data type used to represent text.",
    "variable": "A name that stores a value.",
    "list": "A collection of multiple data elements in an order.",
    "strip": "used to remove, lead, and trail whitespaces.",
    "comments": "A written description used to clarify and enhance comprehension of the code.",
}

#Printing each value of variable in dictionary "glossary" with a blank line in between
for term, definition in glossary.items():
    print(f"{term}:\n{definition}\n")
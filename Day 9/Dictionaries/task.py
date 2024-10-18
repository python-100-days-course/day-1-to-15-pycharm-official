programming_dictionary = {
    "Bug": "An error in a program that prevents the program from running as expected.",
    "Function": "A piece of code that you can easily call over and over again.",
}

# Enter the key to retrieve the corresponding value in a dictionary
print(programming_dictionary["Bug"])

print(type(programming_dictionary))

# To add to dictionary
programming_dictionary["Loop"] = "The action of doing something over and over again."
print(f"programming_dictionary = {programming_dictionary}")

empty_dictionary = {}

# Wipe an existing dictionary
# programming_dictionary = {}
# print(f"programming_dictionary = {programming_dictionary}")

# Edit an item in a dictionary
programming_dictionary["Bug"] = "A moth in your computer"
print(f"programming_dictionary = {programming_dictionary}")

# Loop through a dictionary
for key in programming_dictionary:
    print(key)
    print(programming_dictionary[key])

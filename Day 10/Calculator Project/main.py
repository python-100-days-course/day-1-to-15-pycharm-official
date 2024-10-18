from art import logo
print(logo)

def add(n1, n2):
    """Add two numbers."""
    return n1 + n2
# TODO-1: Write out the other 3 functions - subtract, multiply and divide.
def subtract(n3, n4):
    """Subtract two numbers."""
    return n3 - n4
def divide(n5, n6):
    """Divide two numbers."""
    return n5 / n6
def multiply(n7, n8):
    """Multiply two numbers."""
    return n7 * n8
# print(f"1+2={add(1,2)}, 7-4={subtract(7,4)}, 21/7={divide(21,7)}, 6*9={multiply(6,9)}")

# version 2
# TODO-2: Add these 4 functions into a dictionary as the values. Keys = "+", "-", "*", "/"
# note: parenthesis for functions are excluded to not trigger them
operations_dictionary =  {"+": add, "-": subtract, "*": multiply, "/": divide}
# print(operations_dictionary["*"](3,2)) # check

# TODO-3: Use the dictionary operations to perform the calculations. Multiply 4 * 8 using the dictionary.
# print(f'4 * 8 = {operations_dictionary["*"](4,8)}')

# version 2 - works
# Note: v1 was created following step by step instructions
calculating = True
cont_calc = "n"
num1 = 0
num2 = 0
operation = ""
result = 0
while calculating:
    # check if it's a continuation of a previous calculation, if no, then ask for a number:
    if cont_calc == "n":
        num1 = float(input("What's the first number?: "))
    print("+\n-\n*\n/")
    operation = input("Pick an operation: ")
    num2 = float(input("What's the next number?: "))
    # print(f"num1 = {num1}\nnum2 = {num2}\noperation = {operation}") # check
    if operation not in operations_dictionary:
        print("Error: You must have typed an incorrect operator, please try again.")
        continue # start the while loop from beginning
    result = operations_dictionary[operation](num1,num2)
    print(f"{num1} {operation} {num2} = {result}")
    cont_calc = input(f"Type 'y' to continue calculating with {result}, or type 'n' to start a new calculation: ")
    if cont_calc == "y":
        num1 = result
    elif cont_calc == "n":
        print("\n" * 20) # clear screen
        print(logo)
    else:
        print("Error: Input not recognized, should be 'y' or 'n'.")
        calculating = False

# definition, recursion: to call a function within itself

# # version 1 - works
# # Note: v1 was created without following step by step instructions
# calculating = True
# cont_calc = "n"
# num1 = 0
# num2 = 0
# operation = ""
# result = 0
# while calculating:
#     # check if it's 1st calculation, then ask for a number, otherwise previous result will be used:
#     if cont_calc == "n":
#         num1 = float(input("What's the first number?: "))
#     print("+\n-\n*\n/")
#     operation = input("Pick an operation: ")
#     num2 = float(input("What's the next number?: "))
#     # print(f"num1 = {num1}\nnum2 = {num2}\noperation = {operation}") # check
#     # determine which operations needs to be used and perform the math
#     if operation == "+":
#         result = add(num1, num2)
#     elif operation == "-":
#         result = subtract(num1, num2)
#     elif operation == "*":
#         result = multiply(num1, num2)
#     elif operation == "/":
#         result = divide(num1, num2)
#     else:
#         print("Error: You must have typed an incorrect operator, please try again.")
#         continue # start the while loop from beginning
#     print(f"{num1} {operation} {num2} = {result}")
#     cont_calc = input(f"Type 'y' to continue calculating with {result}, or type 'n' to start a new calculation: ")
#     if cont_calc == "y":
#         num1 = result
#     elif cont_calc != "y" and cont_calc != "n":
#         print("Error: Input not recognized, should be 'y' or 'n'.")
#         calculating = False
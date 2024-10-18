# Title case conversion function:
def format_name(f_name, l_name):
    """Take a first and last name and format it to
    return the title case version of the name."""
    if f_name == "" or l_name == "":
        return "You did not provide valid inputs" # Early return, nothing runs after this
    f_name_formated = f_name.title()
    l_name_formated = l_name.title()
    return f"{f_name_formated} {l_name_formated}"
# formated_string = format_name("jACk", "SPArRoW")
formated_string = format_name(input("What is your first name?"), input("What is your last name?"))
print(formated_string)

# Docstrings: documentation for a function, it's the 1st line in a function, use 3x quotation marks, can be multi line
"""Multi line
comment, should be avoided"""
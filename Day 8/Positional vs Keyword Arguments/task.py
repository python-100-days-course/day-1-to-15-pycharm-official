# Functions with input

# Lesson 62 challenge, multiple parameters:
def greet_with(name, location):
    print(f"Hi {name}.")
    print(f"What is it like in {location}?")
# Positional Arguments:
greet_with("Alex", "Japan")
# Keyword Arguments, order doesn't matter:
greet_with(location="Black Hole", name="Sam")

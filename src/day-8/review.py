# # Simple function
# def greet():
#     print("Hello.")
#     print("How do you do?")
#     print("Isn't the weather nice today?")
#
#
# greet()
#
#
# # Function that allows for input
# def greet_with_name(name):
#     print(f"Hello {name}")
#     print(f"How do you do {name}?")
#     print("Isn't the weather nice today?")
#
#
# name = input("What's your name?")
# greet_with_name(name)

# Function with more than one inputs

def greet_with(name, location):
    print(f"Hello {name}")
    print(f"How do you do {name}?")
    print(f"What is it like in {location}?")


greet_with(location="New York City", name="Angela")

# This is the definition for our function.
# Notice how it takes 2 parameters now.
# The parameters must have different names and must be separated by a comma.
def PrintGreeting(first_name, last_name):
    print("Hello " + first_name + " " + last_name + "!")
 
# Since we have 2 parameters for our function,
# we must now pass two parameters to our function
# when we call it.
first_name = input("Enter first name: ")
last_name = input("Enter last name: ")
PrintGreeting(first_name, last_name)

# This is the definition for our function.
# Notice how we've added a parameter within the parentheses.
# We can name our parameters just like any other variable
# and use them like a regular variable in our functions.
def PrintGreeting(name):
    print("Hello " + name + "!")
 
# We can pass a literal string value directly for
# the parameter when we call the function.
PrintGreeting("Bob")
 
# We can store a string value in a variable and pass
# the variable in for the parameter to the function.
# Note that the variable name here does not have to
# match the name of the parameter of the PrintGreeting()
# function.
name = "John"
PrintGreeting(name)

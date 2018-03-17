# This is the definition for our function.
def PrintGreeting(name):
    print("Hello " + name + "!")
 
# We can get the values we pass for parameters from anywhere.
# In this case, we're getting the value for the name parameter
# from the user.
name = input("Enter a name: ")
PrintGreeting(name)

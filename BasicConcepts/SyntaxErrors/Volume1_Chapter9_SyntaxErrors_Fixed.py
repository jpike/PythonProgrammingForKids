# if statement syntax errors.
if True:
    print("Condition is true!")

if False:
    print("Condition is false!")

strings_are_equal = "ABC" == "ABC"
if strings_are_equal:
    print("Strings are equal!")
else:
    print("Strings are not equal!")

example_number = 2
if 1 == example_number:
    print("Example number is 1.")
elif 2 == example_number:
    print("Example number is 2.")
else:
    print("Example number is some other value.")

if 3 == example_number:
    print("Example number is 3.")
elif 4 == example_number:
    print("Example number is 4")

if strings_are_equal:
    print("Strings are equal!")

if strings_are_equal:
    print("Strings are equal!")
else:
    print("Strings are not equal!")

if strings_are_equal:
    print("Multiline if statement body.")
    print("Here's the second line.")
else:
    print("Multiline else statement body.")
    print("Here's the second line.")

# We start our program by informing the user that this program is for a calculator.
print("Welcome to the calculator program!")
# Our program will run until the user chooses to exit, so we define a variable to
# hold the text that a user must enter to exit the program.  Since we intend that
# this variable be constant (never change), we use uppercase letters, rather than
# lowercase, to differentiate this from our changeable variables.
EXIT_USER_INPUT_OPTION = "EXIT"
# We print out a message to inform the user how to exit the program.
# This string message is formed by combining (concatenating) a string
# literal ("Enter ") with the string stored in our "ENTER_USER_INPUT_OPTION"
# constant with another string literal (" after a calculation to end program.").
# The concatenation is done using the "+" operator.
print("Enter " + EXIT_USER_INPUT_OPTION + " after a calculation to end program.")
# We define a new variable named "user_input_after_calculation" to hold the user's
# input after each calculation.  Since the user hasn't entered any input yet,
# we initialize this variable with an empty string.
user_input_after_calculation = ""
# In order to have our program continue executing until the user chooses to exit,
# we need a loop like a "while" loop.  Since we want our program to exit if
# the user entered text for the exit option (stored in the "EXIT_USER_INPUT_OPTION"
# constant), we checked if this option doesn't equal the user's input (stored in
# the "user_input_after_calculation" variable) using the inequality (or "not equal")
# operator (the "!=" operator).  As long as this boolean condition is True,
# we enter the body of the while loop to execute it.
while EXIT_USER_INPUT_OPTION != user_input_after_calculation:
    # The condition for the while loop is True, so we ask the user to enter the first
    # number to use in the calculation.  This is done using the built-in input() function,
    # which will wait until the user enters some text and then return that text as a string.
    # Since we need numbers to do math in our calculator, we convert that string to an
    # integer using the built-in int() function.  This integer is stored in a variable
    # named "first_number".  This calculator is only supporting integers right now,
    # not floating-point numbers.
    first_number = int(input("Enter first number: "))
    # We need a second number to do math, so we ask the user to enter the second
    # number to use in the calculation.  This is done using the built-in input() function,
    # which will wait until the user enters some text and then return that text as a string.
    # Since we need numbers to do math in our calculator, we convert that string to an
    # integer using the built-in int() function.  This integer is stored in a variable
    # named "second_number".  This calculator is only supporting integers right now,
    # not floating-point numbers.
    second_number = int(input("Enter second number: "))

    # To help make it clear what text users enter correspond to which mathematical operations,
    # we define a constant named "ADDITION_OPERATION" for the addition operation, which we'll
    # represent by the "+" string.
    ADDITION_OPERATION = "+"
    # To help make it clear what text users enter correspond to which mathematical operations,
    # we define a constant named "SUBTRACTION_OPERATION" for the subtraction operation, which we'll
    # represent by the "-" string.
    SUBTRACTION_OPERATION = "-"
    # To help make it clear what text users enter correspond to which mathematical operations,
    # we define a constant named "MULTIPLICATION_OPERATION" for the multiplication operation, which we'll
    # represent by the "*" string.
    MULTIPLICATION_OPERATION = "*"
    # To help make it clear what text users enter correspond to which mathematical operations,
    # we define a constant named "DIVISION_OPERATION" for the division operation, which we'll
    # represent by the "/" string.
    DIVISION_OPERATION = "/"
    # To help users know which operations our calculator supports, we print out a message prior
    # to printing out the valid operations.
    print("Valid operations include: ")
    # Print out the addition operation to inform the user of it.
    print(ADDITION_OPERATION)
    # Print out the subtraction operation to inform the user of it.
    print(SUBTRACTION_OPERATION)
    # Print out the multiplication operation to inform the user of it.
    print(MULTIPLICATION_OPERATION)
    # Print out the division operation to inform the user of it.
    print(DIVISION_OPERATION)

    # Ask the user to enter an operation.  This will print out a message and then wait
    # for the user to enter some text using the built-in input() function.  The input()
    # function will return the string text that the user entered, which we store in a
    # new "operation" variable.
    operation = input("Enter an operation: ")

    # This "if" statement checks if the user entered an addition operation by checking
    # if the string in our "ADDITION_OPERATION" constant is equal to the operation stored
    # in the "operation" variable.  This is done using the equality ("==") operator, which
    # will return True if the values are equal and False if not equal.
    if ADDITION_OPERATION == operation:
        # Perform the addition operation using the "+" operator to calculate the
        # sum of the numbers.  The value stored in the "first_number" variable is
        # added to the value stored in the "second_number" variable, and the result
        # is stored in the "sum_result" variable.
        sum_result = first_number + second_number
        # Print the sum to the screen to inform the user of the calculated result.  
        # This is done by combining a string literal with the value stored in
        # the "sum_result" variable.  Since the value in the "sum_result" variable
        # is a number, not a string, we need to convert it to a string using the
        # built-in str() function before combining it with the string literal.
        # The final combined message is passed to the built-in print() function
        # to print it to the screen.
        print("The sum is: " + str(sum_result))
    # The operation in the previous "if" statement wasn't chosen, so this "elif"
    # statement checks if the user entered a subtraction operation by checking
    # if the string in our "SUBTRACTION_OPERATION" constant is equal to the operation stored
    # in the "operation" variable.  This is done using the equality ("==") operator, which
    # will return True if the values are equal and False if not equal.
    elif SUBTRACTION_OPERATION == operation:
        # Perform the subtraction operation using the "-" operator to calculate the
        # difference of the numbers.  The value stored in the "second_number" variable is
        # subtracted from the value stored in the "first_number" variable, and the result
        # is stored in the "difference_result" variable.
        difference_result = first_number - second_number
        # Print the difference to the screen to inform the user of the calculated result.  
        # This is done by combining a string literal with the value stored in
        # the "difference_result" variable.  Since the value in the "difference_result" variable
        # is a number, not a string, we need to convert it to a string using the
        # built-in str() function before combining it with the string literal.
        # The final combined message is passed to the built-in print() function
        # to print it to the screen.
        print("The difference is: " + str(difference_result))
    # The operations in the previous "if" and "elif" statement weren't chosen, so this "elif"
    # statement checks if the user entered a multiplication operation by checking
    # if the string in our "MULTIPLICATION_OPERATION" constant is equal to the operation stored
    # in the "operation" variable.  This is done using the equality ("==") operator, which
    # will return True if the values are equal and False if not equal.
    elif MULTIPLICATION_OPERATION == operation:
        # Perform the multiplication operation using the "*" operator to calculate the
        # product of the numbers.  The value stored in the "first_number" variable is
        # multiplied by the value stored in the "second_number" variable, and the result
        # is stored in the "product_result" variable.
        product_result = first_number * second_number
        # Print the difference to the screen to inform the user of the calculated result.  
        # This is done by combining a string literal with the value stored in
        # the "product_result" variable.  Since the value in the "product_result" variable
        # is a number, not a string, we need to convert it to a string using the
        # built-in str() function before combining it with the string literal.
        # The final combined message is passed to the built-in print() function
        # to print it to the screen.
        print("The product is: " + str(product_result))
    # The operations in the previous "if" and "elif" statement weren't chosen, so this "elif"
    # statement checks if the user entered a division operation by checking
    # if the string in our "DIVISION_OPERATION" constant is equal to the operation stored
    # in the "operation" variable.  This is done using the equality ("==") operator, which
    # will return True if the values are equal and False if not equal.
    elif DIVISION_OPERATION == operation:
        # Perform the division operation using the "/" operator to calculate the
        # quotient of the numbers.  The value stored in the "first_number" variable is
        # divided by the value stored in the "second_number" variable, and the result
        # is stored in the "quotient_result" variable.
        quotient_result = first_number / second_number
        # Print the difference to the screen to inform the user of the calculated result.  
        # This is done by combining a string literal with the value stored in
        # the "quotient_result" variable.  Since the value in the "quotient_result" variable
        # is a number, not a string, we need to convert it to a string using the
        # built-in str() function before combining it with the string literal.
        # The final combined message is passed to the built-in print() function
        # to print it to the screen.
        print("The quotient is: " + str(quotient_result))
    # None of the operations checked for in the previous "if" or "elif" statements were
    # chosen, so this "else" statement provides a way to handle the user entering
    # some other invalid text.
    else:
        # To inform the user that his/her entered operation is invalid, we print out a message
        # indicating the entered text (operation) that was invalid.  This is done by concatenating
        # a string literal with a string variable (operation) with another string literal.
        print('The "' + operation + '" operation is invalid.')

    # A calculation has finished being performed, so we ask the user for input using the built-in
    # input() function to determine if this calculator program should continue executing or exit.
    # The message we print out using the input() function includes the value in our "EXIT_USER_INPUT_OPTION"
    # constant to let the user know exactly what text needs to be entered to exit.  Since the condition
    # for our "while" loop above only checks for this EXIT_USER_INPUT_OPTION, the user can enter
    # any other text to continue executing and perform another calculation.  After the user enters
    # some text, the string value entered will be returned from the input() function and stored
    # in the "user_input_after_calculation" variable.
    user_input_after_calculation = input("Enter " + EXIT_USER_INPUT_OPTION + " to end program or any other text to perform another calculation.")

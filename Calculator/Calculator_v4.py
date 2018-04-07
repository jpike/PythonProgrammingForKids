# INFORM THE USER ABOUT HOW THIS PROGRAM WORKS.
# A special input option exists for exiting the program.
print("Welcome to the calculator program!")
EXIT_USER_INPUT_OPTION = "EXIT"
print("Enter " + EXIT_USER_INPUT_OPTION + " after a calculation to end program.")
user_input_after_calculation = ""
while EXIT_USER_INPUT_OPTION != user_input_after_calculation:
    # GET TWO NUMBERS FROM THE USER.
    # Note that this calculator is assuming only integers can be entered.
    # If you want to support floating-point numbers (numbers with digits
    # after the decimal point), change "int" to "float" in the lines below.
    first_number = int(input("Enter first number: "))
    second_number = int(input("Enter second number: "))

    # INFORM THE USER OF VALID OPERATIONS.
    ADDITION_OPERATION = "+"
    SUBTRACTION_OPERATION = "-"
    MULTIPLICATION_OPERATION = "*"
    DIVISION_OPERATION = "/"
    print("Valid operations include: ")
    print(ADDITION_OPERATION)
    print(SUBTRACTION_OPERATION)
    print(MULTIPLICATION_OPERATION)
    print(DIVISION_OPERATION)

    # GET THE OPERATION FROM THE USER.
    operation = input("Enter an operation: ")

    # PERFORM THE MATH OPERATION ON THE NUMBERS.
    # Note that since "sum" is a built-in Python function,
    # a "_result" suffix is added to variable names below
    # to avoid hiding the built-in sum() function.
    if ADDITION_OPERATION == operation:
        # PRINT THE SUM.
        sum_result = first_number + second_number
        print("The sum is: " + str(sum_result))
    elif SUBTRACTION_OPERATION == operation:
        # PRINT THE DIFFERENCE.
        difference_result = first_number - second_number
        print("The difference is: " + str(difference_result))
    elif MULTIPLICATION_OPERATION == operation:
        # PRINT THE PRODUCT.
        product_result = first_number * second_number
        print("The product is: " + str(product_result))
    elif DIVISION_OPERATION == operation:
        # PRINT THE QUOTIENT.
        quotient_result = first_number / second_number
        print("The quotient is: " + str(quotient_result))
    else:
        # INFORM THE USER THAT THE OPERATION IS INVALID.
        print('The "' + operation + '" operation is invalid.')

    # SEE IF THE USER WANTS TO CONTINUE.
    user_input_after_calculation = input("Enter " + EXIT_USER_INPUT_OPTION + " to end program or any other text to perform another calculation.")

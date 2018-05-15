print("Welcome to the calculator program!")
EXIT_USER_INPUT_OPTION = "EXIT"
print("Enter " + EXIT_USER_INPUT_OPTION + " after a calculation to end program.")
user_input_after_calculation = ""
while EXIT_USER_INPUT_OPTION != user_input_after_calculation:
    first_number = int(input("Enter first number: "))
    second_number = int(input("Enter second number: "))

    ADDITION_OPERATION = "+"
    SUBTRACTION_OPERATION = "-"
    MULTIPLICATION_OPERATION = "*"
    DIVISION_OPERATION = "/"
    print("Valid operations include: ")
    print(ADDITION_OPERATION)
    print(SUBTRACTION_OPERATION)
    print(MULTIPLICATION_OPERATION)
    print(DIVISION_OPERATION)

    operation = input("Enter an operation: ")

    if ADDITION_OPERATION == operation:
        sum_result = first_number + second_number
        print("The sum is: " + str(sum_result))
    elif SUBTRACTION_OPERATION == operation:
        difference_result = first_number - second_number
        print("The difference is: " + str(difference_result))
    elif MULTIPLICATION_OPERATION == operation:
        product_result = first_number * second_number
        print("The product is: " + str(product_result))
    elif DIVISION_OPERATION == operation:
        quotient_result = first_number / second_number
        print("The quotient is: " + str(quotient_result))
    else:
        print('The "' + operation + '" operation is invalid.')

    user_input_after_calculation = input("Enter " + EXIT_USER_INPUT_OPTION + " to end program or any other text to perform another calculation.")

# GET TWO NUMBERS FROM THE USER.
# Note that this calculator is assuming only integers can be entered.
# If you want to support floating-point numbers (numbers with digits
# after the decimal point), change "int" to "float" in the lines below.
first_number = int(input("Enter first number: "))
second_number = int(input("Enter second number: "))

# GET THE OPERATION FROM THE USER.
operation = input("Enter an operation: ")

# PERFORM THE MATH OPERATION ON THE NUMBERS.
ADDITION_OPERATION = "+"
SUBTRACTION_OPERATION = "-"
MULTIPLICATION_OPERATION = "*"
DIVISION_OPERATION = "/"
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

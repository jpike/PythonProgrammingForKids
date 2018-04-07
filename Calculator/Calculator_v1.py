# GET TWO NUMBERS FROM THE USER.
# Note that this calculator is assuming only integers can be entered.
# If you want to support floating-point numbers (numbers with digits
# after the decimal point), change "int" to "float" in the lines below.
first_number = int(input("Enter first number: "))
second_number = int(input("Enter second number: "))

# PERFORM DIFFERENT MATH OPERATIONS ON THE NUMBERS.
# Note that since "sum" is a built-in Python function,
# a "_result" suffix is added to variable names below
# to avoid hiding the built-in sum() function.
sum_result = first_number + second_number
print("The sum of " + str(first_number) + " + " + str(second_number) + " is " + str(sum_result))
difference_result = first_number - second_number
print("The difference of " + str(first_number) + " - " + str(second_number) + " is " + str(difference_result))
product_result = first_number * second_number
print("The product of " + str(first_number) + " * " + str(second_number) + " is " + str(product_result))
quotient_result = first_number / second_number
print("The quotient of " + str(first_number) + " / " + str(second_number) + " is " + str(quotient_result))

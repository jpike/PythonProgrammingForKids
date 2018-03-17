def Add(first_number, second_number):
    # Notice how we're calculating a value, storing that value in a variable,
    # and then returning the variable.
    sum_of_numbers = first_number + second_number
    return sum_of_numbers

# Here we're getting 2 floating-point numbers (numbers that can have
# fractional components or components on the right of the decimal point).
# These 2 numbers will get added together when we call our function. 
a_number = float(input("Enter a number: "))
another_number = float(input("Enter another number: "))
sum_result = Add(a_number, another_number)
print(sum_result)

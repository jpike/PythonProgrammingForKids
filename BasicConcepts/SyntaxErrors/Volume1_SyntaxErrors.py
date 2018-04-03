# Print statements with syntax errors.
print(Hello, world!)
print('This is a series)
print(of print statements.')
    print('The end!')
print('But not really!")
print("Here's another print statement!')
print("And here's another one!"
print "This will be the last one of these initial print statements.")

# String variable statements with syntax errors.
string variable = 'This line should have a string variable.'
1string_variable_2 = "This line should have another string variable."
another_string_variable = 'This line has another string variable."
yet_another_string_variable = "This line has yet another string variable.'
first_string_variable_to_print = This string variable should be printed on the next line
print(first_strng_variable_to_print)
print("Here is the string variable's value again: " + first_strng_variable_to_print)
combined_strings = "Here's a case where multiple strings " + string_variable + first_string_variable_to_print " are being combined"
print(combined_strings)

# User input lines with syntax errors.
user_input = input(Now we are trying user input.  Enter a value: )
print(user_input)

# String/math operation errors.
# Some of the lines below have runtime errors, rather than syntax errors.
combined_numeric_strings = '1' + 1
print(combined_numeric_strings)
combined_numbers = 1 + '1'
print(combined_numbers)
difference = '5' - '2'
print(difference)
product = '2' * '3'
print(product)
quotient = '9' / '4'
print(quotient)

# Commenting syntax errors.
print("Printing out a message!" # This is a comment.)
floating_point_number = 1.5 * # 2.7

# Boolean (comparison) operator syntax errors.
values_are_equal = 1 = = 1
values_are_not_equal = 1 ! = 2
left_is_less_than_right = 1 2 <
left_is_greater_than_right = < 2 1
left_is_less_than_or_equal_to_right = 1 < = 2
left_is_greater_than_or_equal_to_right = 2 > = 2

# type() function call syntax errors.
print(type(1)
print(type"ABC"))
print(typeFalse)

# if statement syntax errors.
if true:
    print("Condition is true!")

if false:
    print("Condition is false!")

strings_are_equal = "ABC" == "ABC"
if strings_are_equal
    print("Strings are equal!")
else
    print("Strings are not equal!")

example_number = 2
if 1 == example_number:
    print("Example number is 1.")
elseif 2 == example_number:
    print("Example number is 2.")
else:
    print("Example number is some other value.")

if 3 == example_number:
    print("Example number is 3.")
elif 4 == example_number
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

# While loop syntax errors.
while False
    print("In body of while loop!")

example_number = 2
while example_number < 5:
print("In body of while loop!")
example_number = example_number + 1

while example_number < 10:
        print("In body of while loop!")
      print("Here's another line!")
    print(example_number)
    example_number += 1

while example_number < 15:
    example_number_is_even = example_number % 2 == 0
    if example_number_is_even:
            break

        example_number += 1

# For loop syntax errors.
for iteration range(5):
    print(iteration)

for iteration in range(5)
    print(iteration)

for iteration in range(5):
        print(iteration)

for iteration in range(5):
  print(iteration)
    print(iteration * 2)

for iteration in range(2 10):
    print(iteration)

for iteration in range(2; 10):
    print(iteration)

for iteration in range(5, 10):
    print(iteration)
        if True:
        print("Printing after iteration!")
        else:
            break

# String variable statements with syntax errors.
string_variable = 'This line should have a string variable.'
string_variable_2 = "This line should have another string variable."
another_string_variable = 'This line has another string variable.'
yet_another_string_variable = "This line has yet another string variable."
first_string_variable_to_print = "This string variable should be printed on the next line"
print(first_string_variable_to_print)
print("Here is the string variable's value again: " + first_string_variable_to_print)
combined_strings = "Here's a case where multiple strings " + string_variable + first_string_variable_to_print + " are being combined"
print(combined_strings)

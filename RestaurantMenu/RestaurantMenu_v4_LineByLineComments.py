# Defines a function with the name "GetPaymentFromUser" that takes one parameter named "order_total_in_dollars_and_cents".
def GetPaymentFromUser(order_total_in_dollars_and_cents):
    # Creates a new variable to hold the payment amount from the user (in units of dollars and cents).
    # The variable is initialized with an initial value of zero to indicate that the user hasn't added any payment yet.
    payment_amount_in_dollars_and_cents = 0.0
    # This "while" loop will repeatedly execute as long as the user's payment amount (stored in the
    # "payment_amount_in_dollars_and_cents" variable) isn't enough (is less than) the total for the order
    # (stored in the "order_total_in_dollars_and_cents" variable).  If the user enters enough money as
    # payment, then this less-than condition will be false, so the loop will not be entered again.
    while payment_amount_in_dollars_and_cents < order_total_in_dollars_and_cents:
        # Prompts the user to enter a payment amount (displaying "Enter payment amount: " on the screen)
        # and then waits and gets input from the user (whatever the user types in).  It is assumed that
        # the user will enter a floating-point numeric value (a number possibly with digits after the
        # decimal point), so the built-in float() function is called on the string value returned
        # from the input(0 function to convert it to a numeric value we can use.  The numeric value
        # entered by the user is then stored in the "payment_amount_in_dollars_and_cents" variable.
        payment_amount_in_dollars_and_cents = float(input('Enter payment amount: '))

        # Checks if the payment amount entered by the user (stored in the "payment_amount_in_dollars_and_cents"
        # variable) is enough (greater than or equal to) to cover the total cost of the order (stored in the
        # order_total_in_dollars_and_cents variable).  The return value of this >= (greater than or equal to)
        # comparison is a boolean (True or False) value that gets stored in the new "payment_amount_enough"
        # variable).
        payment_amount_enough = payment_amount_in_dollars_and_cents >= order_total_in_dollars_and_cents
        # Checks the boolean value stored in the "payment_amount_enough" variable to see if the payment amount
        # entered by the user is NOT enough to cover the cost of the order.
        if not payment_amount_enough:
            # Since the above condition is True (the payment amount isn't enough to cover the total cost
            # of the order), the message below is printed out to the screen for the user to indicate
            # that he/she didn't enter a high enough payment amount.
            print('Not enough to pay for order.')

    # At this point, the above "while" loop has exited since it's less-than condition is False, which means
    # that the user has entered a sufficient payment amount (stored in the "payment_amount_in_dollars_and_cents"
    # variable) to cover the cost of the order.  To make this payment amount available to code calling this
    # "GetPaymentFromUser" function, we "return" the value stored in the payment_amount_in_dollars_and_cents variable,
    # which exits the function.
    return payment_amount_in_dollars_and_cents

# The above code was just defining a function (saying the function with a particular name exists), not actually executing it.
# That means that when we execute this Python program, execution will really start at the line below, which prints out a message
# to the screen welcoming the user to our particular restaurant.
print('Welcome to Food Funhouse!')

# Creates a new local variable named "order_total_in_dollars_and_cents" to hold the total price of the user's order
# (in units of dollars and cents).  It is assigned an initial value of zero to indicate that the user hasn't ordered
# anything yet.
order_total_in_dollars_and_cents = 0.0
# A loop is started to continue executing code within the loop's body while (as long as) the condition "True"
# is "True".  This is designed to have this program continue executing until the user explicitly chooses to
# exit within the body of the loop, which will then result in breaking out of the loop and exiting the program.
while True:
    # Prints out the 1st menu item that the user can select.  The item is designed to be selected
    # when the user enters "1".  This item is a cheeseburger that costs $5.50.
    print('1. Cheeseburger - $5.50')
    # Prints out the 2nd menu item that the user can select.  The item is designed to be selected
    # when the user enters "2".  This item is a pizza that costs $5.00.
    print('2. Pizza - $5.00')
    # Prints out the 3rd menu item that the user can select.  The item is designed to be selected
    # when the user enters "3".  This item is a taco that costs $3.00.
    print('3. Taco - $3.00')
    # Prints out the 4th menu item that the user can select.  The item is designed to be selected
    # when the user enters "4".  This item is a cookie that costs $1.99.
    print('4. Cookie - $1.99')
    # Prints out the 5th menu item that the user can select.  The item is designed to be selected
    # when the user enters "5".  This item is a pizza that costs $0.99.
    print('5. Milk - $0.99')
    # Prints out the 6th menu option that the user can select.  The option is designed to be selected
    # when the user enters "6".  Unlike previous menu options, this option is to provide a way for
    # the user to pay for his/her order (and then exit the program).
    print('6. Pay for Order/Exit')
    # Prints out the 7th menu option that the user can select.  The option is designed to be selected
    # when the user enters "7".  Unlike previous menu options, this option is to provide a way for
    # the user to cancel his/her order in case an error was made in ordering (and then exit the program).
    print('7. Cancel Order/Exit')

    # Asks the user to input one of the above menu options.  This will wait until the user
    # enters some text and then presses the "enter" key.  Once the user finishes entering
    # text, the built-in input() function will return a string value.  Since all of the
    # above menu options expect integer numeric options, the return value is converted
    # to an integer with the built-in int() function to get the menu option selected
    # by the user (which is stored in a new variable named "selected_menu_option").
    selected_menu_option = int(input('Select an item to order: '))

    # Checks if the menu option selected by the user (stored in the "selected_menu_option" variable)
    # is the 1st menu option (indicated by an integer 1 value).  This is done using an equality
    # comparison (using the "==" operator) to see if 1 equals the selected menu option.
    if 1 == selected_menu_option:
        # Menu option 1 was selected, so this adds the price of the 1st menu item (the cheeseburger)
        # to the price of the user's total order (stored in the variable "order_total_in_dollars_and_cents").
        # The price of this menu item is $5.50, as indicated in the print() statement above.
        # The "+=" operator is used to add the 5.50 value to the value already stored in the variable.
        order_total_in_dollars_and_cents += 5.50
        # To provide helpful feedback to the user, we print information about what he/she just ordered
        # (the cheeseburger) and the total of the order so far.  The first part of the message printed
        # is a string literal in single quotes, but in order to print out the order total (stored in the
        # "order_total_in_dollars_and_cents") variable, we need to convert it to a string using the
        # built-in str() function, and then the string value for the order total is added to the end
        # of the string literal using the "+" operator.  The final string message (a combination of
        # the string literal and the string value for the order total) is passed to the built-in
        # print() function to print the message to the screen.
        print('You ordered a cheeseburger.  Order total: $' + str(order_total_in_dollars_and_cents))
    # If the selected menu option is not 1, then this "elif" (else-if) conditional check is performed,
    # which checks if the menu option selected by the user (stored in the "selected_menu_option" variable)
    # is the 2nd menu option (indicated by an integer 2 value).  This is done using an equality
    # comparison (using the "==" operator) to see if 2 equals the selected menu option.
    elif 2 == selected_menu_option:
        # Menu option 2 was selected, so this adds the price of the 2nd menu item (the pizza)
        # to the price of the user's total order (stored in the variable "order_total_in_dollars_and_cents").
        # The price of this menu item is $5.00, as indicated in the print() statement above.
        # The "+=" operator is used to add the 5.00 value to the value already stored in the variable.
        order_total_in_dollars_and_cents += 5.00
        # To provide helpful feedback to the user, we print information about what he/she just ordered
        # (the pizza) and the total of the order so far.  The first part of the message printed
        # is a string literal in single quotes, but in order to print out the order total (stored in the
        # "order_total_in_dollars_and_cents") variable, we need to convert it to a string using the
        # built-in str() function, and then the string value for the order total is added to the end
        # of the string literal using the "+" operator.  The final string message (a combination of
        # the string literal and the string value for the order total) is passed to the built-in
        # print() function to print the message to the screen.
        print('You ordered a pizza.  Order total: $' + str(order_total_in_dollars_and_cents))
    # If the selected menu option isn't any of the previous options checked if "if" or "elif" conditionals,
    # then this "elif" (else-if) conditional check is performed, which checks if the menu option selected
    # by the user (stored in the "selected_menu_option" variable) is the 3rd menu option (indicated by an
    # integer 3 value).  This is done using an equality comparison (using the "==" operator) to see if 
    # 3 equals the selected menu option.
    elif 3 == selected_menu_option:
        # Menu option 3 was selected, so this adds the price of the 3rd menu item (the taco)
        # to the price of the user's total order (stored in the variable "order_total_in_dollars_and_cents").
        # The price of this menu item is $3.00, as indicated in the print() statement above.
        # The "+=" operator is used to add the 3.00 value to the value already stored in the variable.
        order_total_in_dollars_and_cents += 3.00
        # To provide helpful feedback to the user, we print information about what he/she just ordered
        # (the taco) and the total of the order so far.  The first part of the message printed
        # is a string literal in single quotes, but in order to print out the order total (stored in the
        # "order_total_in_dollars_and_cents") variable, we need to convert it to a string using the
        # built-in str() function, and then the string value for the order total is added to the end
        # of the string literal using the "+" operator.  The final string message (a combination of
        # the string literal and the string value for the order total) is passed to the built-in
        # print() function to print the message to the screen.
        print('You ordered a taco.  Order total: $' + str(order_total_in_dollars_and_cents))
    # If the selected menu option isn't any of the previous options checked if "if" or "elif" conditionals,
    # then this "elif" (else-if) conditional check is performed, which checks if the menu option selected
    # by the user (stored in the "selected_menu_option" variable) is the 4th menu option (indicated by an
    # integer 4 value).  This is done using an equality comparison (using the "==" operator) to see if 
    # 4 equals the selected menu option.
    elif 4 == selected_menu_option:
        # Menu option 4 was selected, so this adds the price of the 4th menu item (the cookie)
        # to the price of the user's total order (stored in the variable "order_total_in_dollars_and_cents").
        # The price of this menu item is $1.99, as indicated in the print() statement above.
        # The "+=" operator is used to add the 1.99 value to the value already stored in the variable.
        order_total_in_dollars_and_cents += 1.99
        # To provide helpful feedback to the user, we print information about what he/she just ordered
        # (the cookie) and the total of the order so far.  The first part of the message printed
        # is a string literal in single quotes, but in order to print out the order total (stored in the
        # "order_total_in_dollars_and_cents") variable, we need to convert it to a string using the
        # built-in str() function, and then the string value for the order total is added to the end
        # of the string literal using the "+" operator.  The final string message (a combination of
        # the string literal and the string value for the order total) is passed to the built-in
        # print() function to print the message to the screen.
        print('You ordered a cookie.  Order total: $' + str(order_total_in_dollars_and_cents))
    # If the selected menu option isn't any of the previous options checked if "if" or "elif" conditionals,
    # then this "elif" (else-if) conditional check is performed, which checks if the menu option selected
    # by the user (stored in the "selected_menu_option" variable) is the 5th menu option (indicated by an
    # integer 5 value).  This is done using an equality comparison (using the "==" operator) to see if 
    # 5 equals the selected menu option.
    elif 5 == selected_menu_option:
        # Menu option 5 was selected, so this adds the price of the 5th menu item (the milk)
        # to the price of the user's total order (stored in the variable "order_total_in_dollars_and_cents").
        # The price of this menu item is $0.99, as indicated in the print() statement above.
        # The "+=" operator is used to add the 0.99 value to the value already stored in the variable.
        order_total_in_dollars_and_cents += 0.99
        # To provide helpful feedback to the user, we print information about what he/she just ordered
        # (the milk) and the total of the order so far.  The first part of the message printed
        # is a string literal in single quotes, but in order to print out the order total (stored in the
        # "order_total_in_dollars_and_cents") variable, we need to convert it to a string using the
        # built-in str() function, and then the string value for the order total is added to the end
        # of the string literal using the "+" operator.  The final string message (a combination of
        # the string literal and the string value for the order total) is passed to the built-in
        # print() function to print the message to the screen.
        print('You ordered milk.  Order total: $' + str(order_total_in_dollars_and_cents))
    # If the selected menu option isn't any of the previous options checked if "if" or "elif" conditionals,
    # then this "elif" (else-if) conditional check is performed, which checks if the menu option selected
    # by the user (stored in the "selected_menu_option" variable) is the 6th menu option (indicated by an
    # integer 6 value).  This is done using an equality comparison (using the "==" operator) to see if 
    # 6 equals the selected menu option.
    elif 6 == selected_menu_option:
        # Menu option 6 was selected, which corresponds to the menu option printed above for paying
        # for the order and then exiting the program.  We start by printing out the order total
        # as part of a helpful message so that the user knows the final price of his/her order.
        # The first part of the message printed is a string literal in single quotes, but in order
        # to print out the order total (stored in the "order_total_in_dollars_and_cents") variable,
        # we need to convert it to a string using the built-in str() function, and then the string 
        # value for the order total is added to the end of the string literal using the "+" operator.
        # The final string message (a combination of the string literal and the string value for the
        # order total) is passed to the built-in print() function to print the message to the screen.
        print('Your order total is $' + str(order_total_in_dollars_and_cents))
        # We now need to get payment from the user.  In order to do this, we call our "GetPaymentFromUser"
        # function that was defined above, passing in the order total (stored in the "order_total_in_dollars_and_cents"
        # variable) for the function's parameter.  When this function eventually returns, it will
        # return the floating-point number for the payment amount entered by the user, which we store
        # in a new variable named "payment_amount_in_dollars_and_cents".
        payment_amount_in_dollars_and_cents = GetPaymentFromUser(order_total_in_dollars_and_cents)
        # The user might have entered more money for his/her payment than the order's total, so we need
        # to calculate change.  This is done by subtracting the order's total price (stored in the
        # "order_total_in_dollars_and_cents" variable) from the user's payment amount (stored in the
        # "payment_amount_in_dollars_and_cents" variable) using the "-" operator.  The resulting
        # change that is calculated from this subtraction is stored in a new variable named
        # "change_in_dollars_and_cents".
        change_in_dollars_and_cents = payment_amount_in_dollars_and_cents - order_total_in_dollars_and_cents
        # We thank the user for paying for the order by printing a message to the screen.
        print('Thanks for paying!')
        # We next print out how much change the user gets after paying for his/her order.
        # The first part of the message printed is a string literal in single quotes, but in order
        # to print out the change (stored in the "change_in_dollars_and_cents") variable,
        # we need to convert it to a string using the built-in str() function, and then the string 
        # value for the change is added to the end of the string literal using the "+" operator.
        # The final string message (a combination of the string literal and the string value for the
        # order total) is passed to the built-in print() function to print the message to the screen.
        print('Your change is $' + str(change_in_dollars_and_cents))
        # This menu option (#6) that was selected by the user is designed to exit the program
        # after the order has been payed for.  Therefore, we use a "break" statement to break
        # out of our "while True" loop, which will cause the program to exit since we don't have
        # any code after the while loop.
        break
    # If the selected menu option isn't any of the previous options checked if "if" or "elif" conditionals,
    # then this "elif" (else-if) conditional check is performed, which checks if the menu option selected
    # by the user (stored in the "selected_menu_option" variable) is the 7th menu option (indicated by an
    # integer 7 value).  This is done using an equality comparison (using the "==" operator) to see if 
    # 7 equals the selected menu option.     
    elif 7 == selected_menu_option:
        # Menu option 7 was selected, which corresponds to the menu option printed above for cancelling
        # the order and then exiting the program.  Since nothing needs to be done to cancel the order,
        # we just print out a helpful message to the user to indicate that the program is exiting.
        print('Exiting...')
        # This menu option (#7) that was selected by the user is designed to exit the program
        # Therefore, we use a "break" statement to break out of our "while True" loop, which 
        # will cause the program to exit since we don't have any code after the while loop.
        break
    # This "else" clause is provided to provide some behavior that occurs if the selected menu option isn't
    # any of the previous options checked if "if" or "elif" conditionals.  In other words, this "else"
    # clause is provided to handle the case where the user doesn't enter a valid menu option.
    else:
        # The user didn't enter a valid menu option, so we print out a message to let him/her know
        # that the selection was invalid.  We also invite him/her to try entering another option.
        print('Invalid selection.  Please try again.')


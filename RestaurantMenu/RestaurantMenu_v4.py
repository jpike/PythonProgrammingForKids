## Gets a payment amount from the user.
## This function will loop until the user enters a payment amount that is
## enough to cover the provided order total.
## \param[in]   order_total_in_dollars_and_cents - A floating-point number
##      for total amount of money for the order that the user has to pay for.
## \return  A floating-point number (in dollars and cents) for a sufficient
##      payment amount entered by the user for paying for the order.
def GetPaymentFromUser(order_total_in_dollars_and_cents):
    # WAIT UNTIL THE USER INPUTS ENOUGH MONEY TO PAY FOR THE ORDER.
    payment_amount_in_dollars_and_cents = 0.0
    while payment_amount_in_dollars_and_cents < order_total_in_dollars_and_cents:
        # GET THE PAYMENT AMOUNT FROM THE USER.
        payment_amount_in_dollars_and_cents = float(input('Enter payment amount: '))

        # INFORM THE USER IF THE PAYMENT AMOUNT ISN'T ENOUGH.
        payment_amount_enough = payment_amount_in_dollars_and_cents >= order_total_in_dollars_and_cents
        if not payment_amount_enough:
            print('Not enough to pay for order.')

    return payment_amount_in_dollars_and_cents

# PRINT OUT A WELCOME MESSAGE.
print('Welcome to Food Funhouse!')

# LOOP UNTIL THE USER CHOOSES TO EXIT.
order_total_in_dollars_and_cents = 0.0
while True:
    # PRINT OUT THE MENU OPTIONS.
    print('1. Cheeseburger - $5.50')
    print('2. Pizza - $5.00')
    print('3. Taco - $3.00')
    print('4. Cookie - $1.99')
    print('5. Milk - $0.99')
    print('6. Pay for Order/Exit')
    print('7. Cancel Order/Exit')

    # LET THE USER SELECT A MENU OPTION.
    selected_menu_option = int(input('Select an item to order: '))

    # PRINT OUT THE OPTION THE USER SELECTED.
    if 1 == selected_menu_option:
        order_total_in_dollars_and_cents += 5.50
        print('You ordered a cheeseburger.  Order total: $' + str(order_total_in_dollars_and_cents))
    elif 2 == selected_menu_option:
        order_total_in_dollars_and_cents += 5.00
        print('You ordered a pizza.  Order total: $' + str(order_total_in_dollars_and_cents))
    elif 3 == selected_menu_option:
        order_total_in_dollars_and_cents += 3.00
        print('You ordered a taco.  Order total: $' + str(order_total_in_dollars_and_cents))
    elif 4 == selected_menu_option:
        order_total_in_dollars_and_cents += 1.99
        print('You ordered a cookie.  Order total: $' + str(order_total_in_dollars_and_cents))
    elif 5 == selected_menu_option:
        order_total_in_dollars_and_cents += 0.99
        print('You ordered milk.  Order total: $' + str(order_total_in_dollars_and_cents))
    elif 6 == selected_menu_option:
        # PRINT THE ORDER TOTAL.
        print('Your order total is $' + str(order_total_in_dollars_and_cents))

        # GET THE PAYMENT AMOUNT FROM THE USER.
        payment_amount_in_dollars_and_cents = GetPaymentFromUser(order_total_in_dollars_and_cents)

        # CALCULATE THE CHANGE FOR THE ORDER.
        change_in_dollars_and_cents = payment_amount_in_dollars_and_cents - order_total_in_dollars_and_cents

        # INFORM THE USER OF THEIR CHANGE.
        print('Thanks for paying!')
        print('Your change is $' + str(change_in_dollars_and_cents))
        break
            
    elif 7 == selected_menu_option:
        print('Exiting...')
        break
    else:
        print('Invalid selection.  Please try again.')


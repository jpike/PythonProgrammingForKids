# A new variable named "player_1_score" is created to hold player 1's score.
# It is assigned an initial value of 0 since the game is just starting and
# player 1 hasn't scored any points yet.
player_1_score = 0
# A new variable named "player_2_score" is created to hold player 2's score.
# It is assigned an initial value of 0 since the game is just starting and
# player 2 hasn't scored any points yet.
player_2_score = 0

# Since our game is going to loop (continue to exit) until the player chooses to exit,
# and we're going to check for the user choosing to exit in the body of the "while"
# loop below (rather than in the loop's condition), we create a new variable named
# "LOOP_UNTIL_USER_CHOOSES_TO_EXIT_AFTER_A_ROUND" to store the boolean value of
# "True" that we'll use in the condition of the "while" loop (effectively
# creating an infinite loop, if it weren't for us exiting in the body of the
# loop).  Since we intend for the value of this variable to remain constant
# and never change, we use uppercase letters, rather than lowercase, to help
# make that clearer by distinguishing it from our regular variables.  The name
# of this variable (constant) helps improve the readability of our code by
# making the intent of the "while" loops behavior clearer.
LOOP_UNTIL_USER_CHOOSES_TO_EXIT_AFTER_A_ROUND = True
# This is our "while" loop that will keep letting user's playing the game
# until a user chooses to exit, which will happen in the body of the loop
# after each round.
while LOOP_UNTIL_USER_CHOOSES_TO_EXIT_AFTER_A_ROUND:
    # We ask player 1 to choose one of the shapes in a typical "rock", "paper", or "scissors" game.
    # This is done by outputting text identifying the player ("[PLAYER 1]") and then outputting
    # the options as part of a string literal we pass as the prompt to the built-in input() function.
    # This input() function will wait until the user enters some text and then presses the "enter"
    # key on his/her keyboard and then return the text the user entered.  We store this text
    # as a string value in the "player_1_shape" variable.
    player_1_shape = input('[PLAYER 1]: Choose "rock", "paper", or "scissors": ')
    # We ask player 2 to choose one of the shapes in a typical "rock", "paper", or "scissors" game.
    # This is done by outputting text identifying the player ("[PLAYER 2]") and then outputting
    # the options as part of a string literal we pass as the prompt to the built-in input() function.
    # This input() function will wait until the user enters some text and then presses the "enter"
    # key on his/her keyboard and then return the text the user entered.  We store this text
    # as a string value in the "player_2_shape" variable.
    player_2_shape = input('[PLAYER 2]: Choose "rock", "paper", or "scissors": ')

    # We're going to need to check for the "rock" shape in multiple places in the code below.
    # To help ensure consistency each time we check (to help avoid typos), we define another
    # constant variable named "ROCK_SHAPE" to hold the string value we're using for the
    # "rock" choice in the game.  This will also make it easier for us to change the exact
    # string value the user needs to enter for the "rock" by reducing the number of places
    # we'd need to change that value.
    ROCK_SHAPE = 'rock'
    # We're going to need to check for the "paper" shape in multiple places in the code below.
    # To help ensure consistency each time we check (to help avoid typos), we define another
    # constant variable named "PAPER_SHAPE" to hold the string value we're using for the
    # "paper" choice in the game.  This will also make it easier for us to change the exact
    # string value the user needs to enter for the "paper" by reducing the number of places
    # we'd need to change that value.
    PAPER_SHAPE = 'paper'
    # We're going to need to check for the "scissors" shape in multiple places in the code below.
    # To help ensure consistency each time we check (to help avoid typos), we define another
    # constant variable named "SCISSORS_SHAPE" to hold the string value we're using for the
    # "scissors" choice in the game.  This will also make it easier for us to change the exact
    # string value the user needs to enter for the "scissors" by reducing the number of places
    # we'd need to change that value.
    SCISSORS_SHAPE = 'scissors'

    # We next need to check to see if player 1 won this round.  To do this, we create a new
    # variable named "player_1_wins" is created, which will hold a boolean value (True if
    # player 1 won or False if not).  Since we have multiple conditions to check to determine
    # if this player won, we're going to use multiple lines to determine this boolean value.
    # To do this in Python, we need to end this line with an opening parenthesis to indicate
    # that more code related to this line will come on subsequent lines.
    player_1_wins = (
        # In a game of "rock, paper, scissors", a player wins if he/she chooses
        # "rock" while the other player chooses "scissors".  So here we check if
        # player 1 chose rock (by comparing the "ROCK_SHAPE" constant for equality
        # with the value stored in the "player_1_shape" variable) and player 2
        # chose scissors (by comparing the "SCISSORS_SHAPE" constant for equality
        # with the value stored in the "player_2_shape" variable).  These two
        # separate comparisons are joined with the "and" operator to indicate
        # that both must be true and are surrounded by parentheses to keep this
        # check separate from other checks on subsequent lines.  Since we have
        # some additional conditions to check to see if player 1 wins this round,
        # we end this line with the "or" operator to let the player win if the
        # compound condition on this line is true or if one of the conditions on
        # subsequent lines is true.
        (ROCK_SHAPE == player_1_shape and SCISSORS_SHAPE == player_2_shape) or
        # In a game of "rock, paper, scissors", a player wins if he/she chooses
        # "paper" while the other player chooses "rock".  So here we check if
        # player 1 chose paper (by comparing the "PAPER_SHAPE" constant for equality
        # with the value stored in the "player_1_shape" variable) and player 2
        # chose rock (by comparing the "ROCK_SHAPE" constant for equality
        # with the value stored in the "player_2_shape" variable).  These two
        # separate comparisons are joined with the "and" operator to indicate
        # that both must be true and are surrounded by parentheses to keep this
        # check separate from other checks on subsequent lines.  Since we have
        # some additional conditions to check to see if player 1 wins this round,
        # we end this line with the "or" operator to let the player win if the
        # compound condition on this line is true or if one of the conditions on
        # subsequent lines is true.
        (PAPER_SHAPE == player_1_shape and ROCK_SHAPE == player_2_shape) or
        # In a game of "rock, paper, scissors", a player wins if he/she chooses
        # "scissors" while the other player chooses "paper".  So here we check if
        # player 1 chose scissors (by comparing the "SCISSORS_SHAPE" constant for equality
        # with the value stored in the "player_1_shape" variable) and player 2
        # chose paper (by comparing the "PAPER_SHAPE" constant for equality
        # with the value stored in the "player_2_shape" variable).  These two
        # separate comparisons are joined with the "and" operator to indicate
        # that both must be true and are surrounded by parentheses to keep this
        # check separate from other checks on subsequent lines.  This is the last
        # condition we have to check to see if player 1 wins this round,
        # so this line ends with a final closing parenthesis to match up
        # with the opening parenthesis we defined on the line with the
        # "player_1_wins" variable.
        (SCISSORS_SHAPE == player_1_shape and PAPER_SHAPE == player_2_shape))

    # We next need to check to see if player 2 won this round.  To do this, we create a new
    # variable named "player_2_wins" is created, which will hold a boolean value (True if
    # player 1 won or False if not).  Since we have multiple conditions to check to determine
    # if this player won, we're going to use multiple lines to determine this boolean value.
    # To do this in Python, we need to end this line with an opening parenthesis to indicate
    # that more code related to this line will come on subsequent lines.
    player_2_wins = (
        # In a game of "rock, paper, scissors", a player wins if he/she chooses
        # "rock" while the other player chooses "scissors".  So here we check if
        # player 2 chose rock (by comparing the "ROCK_SHAPE" constant for equality
        # with the value stored in the "player_2_shape" variable) and player 1
        # chose scissors (by comparing the "SCISSORS_SHAPE" constant for equality
        # with the value stored in the "player_1_shape" variable).  These two
        # separate comparisons are joined with the "and" operator to indicate
        # that both must be true and are surrounded by parentheses to keep this
        # check separate from other checks on subsequent lines.  Since we have
        # some additional conditions to check to see if player 2 wins this round,
        # we end this line with the "or" operator to let the player win if the
        # compound condition on this line is true or if one of the conditions on
        # subsequent lines is true.
        (ROCK_SHAPE == player_2_shape and SCISSORS_SHAPE == player_1_shape) or
        # In a game of "rock, paper, scissors", a player wins if he/she chooses
        # "paper" while the other player chooses "rock".  So here we check if
        # player 2 chose paper (by comparing the "PAPER_SHAPE" constant for equality
        # with the value stored in the "player_2_shape" variable) and player 1
        # chose rock (by comparing the "ROCK_SHAPE" constant for equality
        # with the value stored in the "player_1_shape" variable).  These two
        # separate comparisons are joined with the "and" operator to indicate
        # that both must be true and are surrounded by parentheses to keep this
        # check separate from other checks on subsequent lines.  Since we have
        # some additional conditions to check to see if player 2 wins this round,
        # we end this line with the "or" operator to let the player win if the
        # compound condition on this line is true or if one of the conditions on
        # subsequent lines is true.
        (PAPER_SHAPE == player_2_shape and ROCK_SHAPE == player_1_shape) or
        # In a game of "rock, paper, scissors", a player wins if he/she chooses
        # "scissors" while the other player chooses "paper".  So here we check if
        # player 2 chose scissors (by comparing the "SCISSORS_SHAPE" constant for equality
        # with the value stored in the "player_2_shape" variable) and player 1
        # chose paper (by comparing the "PAPER_SHAPE" constant for equality
        # with the value stored in the "player_1_shape" variable).  These two
        # separate comparisons are joined with the "and" operator to indicate
        # that both must be true and are surrounded by parentheses to keep this
        # check separate from other checks on subsequent lines.  This is the last
        # condition we have to check to see if player 2 wins this round,
        # so this line ends with a final closing parenthesis to match up
        # with the opening parenthesis we defined on the line with the
        # "player_2_wins" variable.
        (SCISSORS_SHAPE == player_2_shape and PAPER_SHAPE == player_1_shape))

    # It's also possible that both player's tied this round and neither wins.
    # This happens if both players chose the same shape.  We check for this
    # by comparing the shapes chosen by each player (stored in the "player_1_shape"
    # and "player_2_shape" variables) for equality using the "==" operator.
    # This results in a boolean True or False value, which we store in a new
    # variable named "tie".
    tie = (player_1_shape == player_2_shape)

    # We now check if player 1 wins by checking the boolean value in the
    # "player_1_wins" variable in an "if" statement.
    if player_1_wins:
        # Player 1 wins since the condition in the above "if" statement was True,
        # so we print out a message to the players to indicate who won.
        print('PLAYER 1 wins!')
        # Player 1 won this round, so we add 1 point to his/her score (stored in
        # the "player_1_score" variable) using the "+=" operator.
        player_1_score += 1
    # Player 1 didn't win since the condition stored in the "player_1_wins" variable
    # was False when checked in the above "if" statement, so we fall through to this
    # "elif" statement to check if player 2 wins by checking the boolean value in the
    # "player_2_wins" variable.
    elif player_2_wins:
        # Player 2 wins since the condition in the above "elif" statement was True,
        # so we print out a message to the players to indicate who won.
        print('PLAYER 2 wins!')
        # Player 2 won this round, so we add 1 point to his/her score (stored in
        # the "player_2_score" variable) using the "+=" operator.
        player_2_score += 1
    # Neither player won (both the "player_1_wins" and "player_2_wins" variables
    # as checked in the above if/elif statements were False), so now we check if
    # a tie occurred by checking the boolean value in our "tie" variable.
    elif tie:
        # Since a tie occurred (the boolean value stored in the "tie" variable was True
        # when checked in the above "elif" statement), we print out a message to the users
        # to indicate that a tie occurred.
        print('It is a tie!')
    # Due to limited error checking above for our user input, it's possible that our game
    # could not determine a winner or if a tie occurred.  So this "else" clause is provided
    # as a way to handle that situation.
    else:
        # If neither player won nor was there a tie, that likely means at least one user
        # didn't enter a valid choice.  To inform users of that, we print out a message
        # to the screen.
        print('Invalid choices!')

    # The round is over, so we print out player 1's score.
    # The first part of the message printed is a string literal in single quotes, but in order
    # to print out the score (stored in the "player_1_score") variable, we need to convert it
    # to a string using the built-in str() function, and then the string value for the score is
    # added to the end of the string literal using the "+" operator.  The final string message
    # (a combination of the string literal and the string value for the score) is passed to the 
    # built-in print() function to print the message to the screen.
    print("Player 1 Score: " + str(player_1_score))
    # The round is over, so we print out player 2's score.
    # The first part of the message printed is a string literal in single quotes, but in order
    # to print out the score (stored in the "player_2_score") variable, we need to convert it
    # to a string using the built-in str() function, and then the string value for the score is
    # added to the end of the string literal using the "+" operator.  The final string message
    # (a combination of the string literal and the string value for the score) is passed to the 
    # built-in print() function to print the message to the screen.
    print("Player 2 Score: " + str(player_2_score))
    
    # The round is over, so we ask the users if they want to continue playing.  We ask that
    # they enter either "YES" or "NO" using the built-in input() function, which will return
    # a string value after the user enters some text.  This string text will be stored in a
    # new "continue_playing_option" variable.
    continue_playing_option = input("Continue playing? (enter YES or NO): ")
    # We check if the users chose to continue playing by checking if "YES" was entered
    # and stored in the "continue_playing_option" variable using the "==" (equality) operator.
    # If so, this comparsion will evaluate to a boolean True value.
    if "YES" == continue_playing_option:
        # The users entered "YES" to continue playing, so we use a "continue" statement
        # to continue executing our "while" loop, jumping up to the top of the loop
        # where execution of the game will continue.
        continue
    # The users didn't choose to continue, so we now check if the users chose to stop playing
    # by checking if "NO" was entered and stored in the "continue_playing_option" variable using 
    # the "==" (equality) operator.  If so, this comparsion will evaluate to a boolean True value.
    elif "NO" == continue_playing_option:
        # The users entered "NO" to stop playing, so we use a "break" statement to exit out
        # our of our "while" loop.  Since we don't have any code after our while loop,
        # this will cause our program to exit.
        break
    # It's possible the users didn't enter either "YES" or "NO".  To handle this situation,
    # we have an "else" clause added to the end of our "if-elif" chain.
    else:
        # The users didn't enter an invalid choice, so we print out a message indicating this.  
        # For simplicity, we also indicate that the game will exit.
        print("Invalid choice.  Exiting game...")
        # Exit the game using a "break" statement, which will exit out of our "while" loop
        # (and thus exit the program since we don't have any code after the loop).
        break

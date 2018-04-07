# TRACK SCORES FOR EACH PLAYER.
player_1_score = 0
player_2_score = 0

# PLAY THE GAME UNTIL THE PLAYER CHOOSES TO EXIT.
# The exit condition will be checked at the bottom of each loop iteration.
LOOP_UNTIL_USER_CHOOSES_TO_EXIT_AFTER_A_ROUND = True
while LOOP_UNTIL_USER_CHOOSES_TO_EXIT_AFTER_A_ROUND:
    # HAVE EACH PLAYER CHOOSE A SHAPE.
    player_1_shape = input('[PLAYER 1]: Choose "rock", "paper", or "scissors": ')
    player_2_shape = input('[PLAYER 2]: Choose "rock", "paper", or "scissors": ')

    # DEFINE THE DIFFERENT VALID SHAPE CHOICES.
    ROCK_SHAPE = 'rock'
    PAPER_SHAPE = 'paper'
    SCISSORS_SHAPE = 'scissors'

    # DETERMINE WHICH PLAYER WON.
    player_1_wins = (
        (ROCK_SHAPE == player_1_shape and SCISSORS_SHAPE == player_2_shape) or
        (PAPER_SHAPE == player_1_shape and ROCK_SHAPE == player_2_shape) or
        (SCISSORS_SHAPE == player_1_shape and PAPER_SHAPE == player_2_shape))

    player_2_wins = (
        (ROCK_SHAPE == player_2_shape and SCISSORS_SHAPE == player_1_shape) or
        (PAPER_SHAPE == player_2_shape and ROCK_SHAPE == player_1_shape) or
        (SCISSORS_SHAPE == player_2_shape and PAPER_SHAPE == player_1_shape))

    tie = (player_1_shape == player_2_shape)

    # TRACK THE RESULT OF THE GAME.
    if player_1_wins:
        print('PLAYER 1 wins!')
        player_1_score += 1
    elif player_2_wins:
        print('PLAYER 2 wins!')
        player_2_score += 1
    elif tie:
        print('It is a tie!')
    else:
        print('Invalid choices!')

    # PRINT THE SCORES.
    print("Player 1 Score: " + str(player_1_score))
    print("Player 2 Score: " + str(player_2_score))
    
    # DETERMINE IF THE PLAYERS WANT TO CONTINUE PLAYING.
    continue_playing_option = input("Continue playing? (enter YES or NO): ")
    if "YES" == continue_playing_option:
        # CONTINUE TO THE NEXT ROUND OF THE GAME.
        continue
    elif "NO" == continue_playing_option:
        # EXIT THE GAME.
        break
    else:
        # INFORM THE USER OF THE INVALID INPUT AND EXIT THE GAME.
        print("Invalid choice.  Exiting game...")
        break

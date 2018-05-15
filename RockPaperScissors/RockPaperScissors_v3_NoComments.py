player_1_score = 0
player_2_score = 0

LOOP_UNTIL_USER_CHOOSES_TO_EXIT_AFTER_A_ROUND = True
while LOOP_UNTIL_USER_CHOOSES_TO_EXIT_AFTER_A_ROUND:
    player_1_shape = input('[PLAYER 1]: Choose "rock", "paper", or "scissors": ')
    player_2_shape = input('[PLAYER 2]: Choose "rock", "paper", or "scissors": ')

    ROCK_SHAPE = 'rock'
    PAPER_SHAPE = 'paper'
    SCISSORS_SHAPE = 'scissors'

    player_1_wins = (
        (ROCK_SHAPE == player_1_shape and SCISSORS_SHAPE == player_2_shape) or
        (PAPER_SHAPE == player_1_shape and ROCK_SHAPE == player_2_shape) or
        (SCISSORS_SHAPE == player_1_shape and PAPER_SHAPE == player_2_shape))

    player_2_wins = (
        (ROCK_SHAPE == player_2_shape and SCISSORS_SHAPE == player_1_shape) or
        (PAPER_SHAPE == player_2_shape and ROCK_SHAPE == player_1_shape) or
        (SCISSORS_SHAPE == player_2_shape and PAPER_SHAPE == player_1_shape))

    tie = (player_1_shape == player_2_shape)

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

    print("Player 1 Score: " + str(player_1_score))
    print("Player 2 Score: " + str(player_2_score))
    
    continue_playing_option = input("Continue playing? (enter YES or NO): ")
    if "YES" == continue_playing_option:
        continue
    elif "NO" == continue_playing_option:
        break
    else:
        print("Invalid choice.  Exiting game...")
        break

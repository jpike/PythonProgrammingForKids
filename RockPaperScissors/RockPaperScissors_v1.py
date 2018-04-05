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

# INFORM THE PLAYERS OF THE RESULT OF THE GAME.
if player_1_wins:
    print('PLAYER 1 wins!')
elif player_2_wins:
    print('PLAYER 2 wins!')
elif tie:
    print('It is a tie!')
else:
    print('Invalid choices!')
    


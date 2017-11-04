# DISPLAY THE TITLE SCREEN.
# The title screen has a border formed by repeating the character defined below.
TITLE_BORDER_CHARACTER = '#'
TITLE_SCREEN_WIDTH_IN_CHARACTERS = 80
HORIZONTAL_TITLE_BORDER = TITLE_BORDER_CHARACTER * TITLE_SCREEN_WIDTH_IN_CHARACTERS
print(HORIZONTAL_TITLE_BORDER)

# The title screen consists of multiple lines.
TITLE_SCREEN_BODY_HEIGHT_IN_CHARACTERS = 5
for line_index in range(TITLE_SCREEN_BODY_HEIGHT_IN_CHARACTERS):
    # Each line of the title screen body starts with a border on the left.
    current_title_screen_body_line = TITLE_BORDER_CHARACTER

    # The main content of each title screen body line should have a length
    # matching the width of the title screen, minus the 2 characters used
    # for the left/right borders.
    title_screen_body_line_content_character_count = (
        TITLE_SCREEN_WIDTH_IN_CHARACTERS -
        len(TITLE_BORDER_CHARACTER) -
        len(TITLE_BORDER_CHARACTER))

    # Fill the body line content with appropriate content for the line.
    # Two lines within the body of the title screen are special and should
    # have special text inserted in the middle of whitespace.
    TITLE_SCREEN_BODY_FILL_CHARACTER = ' '
    TITLE_SCREEN_BODY_GAME_TITLE_LINE_INDEX = 1
    TITLE_SCREEN_BODY_START_GAME_LINE_INDEX = TITLE_SCREEN_BODY_HEIGHT_IN_CHARACTERS - 2
    if TITLE_SCREEN_BODY_GAME_TITLE_LINE_INDEX == line_index:
        # The content of this line of the title screen body should display the game title.
        GAME_TITLE = 'SPACE COLONY ADVENTURE'
        current_title_screen_body_line += GAME_TITLE.center(
            title_screen_body_line_content_character_count, 
            TITLE_SCREEN_BODY_FILL_CHARACTER )
    elif TITLE_SCREEN_BODY_START_GAME_LINE_INDEX == line_index:
        # The content of this line of the title screen body should tell the player
        # to press the enter key to start.
        current_title_screen_body_line += 'Press Enter to Start'.center(
            title_screen_body_line_content_character_count,
            TITLE_SCREEN_BODY_FILL_CHARACTER )
    else:
        # The content of this line of the title screen body should be filled with whitespace.
        current_title_screen_body_line += (
            TITLE_SCREEN_BODY_FILL_CHARACTER * 
            title_screen_body_line_content_character_count)

    # Each line of the title screen body starts with a border on the right.
    current_title_screen_body_line += TITLE_BORDER_CHARACTER

    print(current_title_screen_body_line)

# After the main body of the title screen, the bottom border should be printed.
print(HORIZONTAL_TITLE_BORDER)

# HAVE THE PLAYER PRESS ENTER TO START.
player_input = input()

# INTRODUCE PLAYERS TO THE GAME.
print("To play, input a 1 to choose the 1st option or a 2 to choose the 2nd option.")
print("Beginning...")

# HAVE THE PLAYER MAKE A DECISION FOR THE FIRST SCENARIO.
print("You wake up one morning on a space colony on the moon of the planet Ewar.  You feel a quake and rumbles.")
print("Choose an option: ")
print("1. Run outside with your space suit on.")
print("2. Stay indoors.")
option = int(input("Input your option now (1 or 2): "))

# RESPOND TO THE OPTION THE PLAYER SELECTED FOR THE SCENARIO.
RUN_OUTSIDE_OPTION = 1
STAY_INDOORS_OPTION = 2
if RUN_OUTSIDE_OPTION == option:
    # HAVE THE PLAYER MAKE A DECISION FOR THE NEXT SCENARIO.
    print("You run outdoors, get on a ship, and escape the planet.")
    print("You land on a planet that appears to be abandoned.")
    print("Choose an option: ")
    print("1. Stay there and leave in the morning after some rest.")
    print("2. Leave now.")
    option = int(input("Input your option now (1 or 2): "))

    # RESPOND TO THE OPTION THE PLAYER SELECTED FOR THE SCENARIO.
    STAY_AND_REST_OPTION = 1
    LEAVE_NOW_OPTION = 2
    if STAY_AND_REST_OPTION == option:
        # HAVE THE PLAYER MAKE A DECISION FOR THE NEXT SCENARIO.
        print("During the night, you see a bright light and hear some rumbling.")
        print("Choose an option: ")
        print("1. Go outside to investigate.")
        print("2. Leave the planet and head towards a bright star.")
        option = int(input("Input your option now (1 or 2): "))

        # RESPOND TO THE OPTION THE PLAYER SELECTED FOR THE SCENARIO.
        GO_OUTSIDE_OPTION = 1
        LEAVE_AND_GO_TO_BRIGHT_START_OPTION = 2
        if GO_OUTSIDE_OPTION == option:
            # HAVE THE PLAYER MAKE A DECISION FOR THE NEXT SCENARIO.
            print("You ran outside and were captured by aliens.")
            print("The aliens put you to work.  You see a friend motioning you over with his hand.")
            print("Choose an option: ")
            print("1. Go over and see what your friend wants.")
            print("2. Continue working.")
            option = int(input("Input your option now (1 or 2): "))

            # RESPOND TO THE OPTION THE PLAYER SELECTED FOR THE SCENARIO.
            SEE_WHAT_FRIEND_WANTS_OPTION = 1
            CONTINUE_WORKING_OPTION = 2
            if SEE_WHAT_FRIEND_WANTS_OPTION == option:
                # HAVE THE PLAYER MAKE A DECISION FOR THE NEXT SCENARIO.
                print("You met up with your friend.  He came up with an escape plan.  You, your family, and friends debate on whether to follow the plan or not.  Some agree with the plan.  Others do not.")
                print("Choose an option: ")
                print("1. Continue debating.")
                print("2. Decide to go along with the plan with only you, your friend, and a few others.")
                option = int(input("Input your option now (1 or 2): "))

                # RESPOND TO THE OPTION THE PLAYER SELECTED FOR THE SCENARIO.
                CONTINUE_DEBATING_OPTION = 1
                GO_ALONG_WITH_PLAN_OPTION = 2
                if CONTINUE_DEBATING_OPTION == option:
                    # HAVE THE PLAYER MAKE A DECISION FOR THE NEXT SCENARIO.
                    print("Everyone reaches agreement with a new plan.  The plan is carried out.  However, near the end of the plan, you notice that you do not have enough escape ships to comfortably seat everyone.")
                    print("Choose an option: ")
                    print("1. Send others and stay behind yourself and a few others.")
                    print("2. Squeeze everyone into ships.")
                    option = int(input("Input your option now (1 or 2): "))

                    # RESPOND TO THE OPTION THE PLAYER SELECTED FOR THE SCENARIO.
                    SEND_OTHERS_AWAY_BUT_STAY_BEHIND_YOURSELF_OPTION = 1
                    SQUEEZE_EVERYONE_INTO_SHIPS_OPTION = 2
                    if SEND_OTHERS_AWAY_BUT_STAY_BEHIND_YOURSELF_OPTION == option:
                        print("You and a few others remain stuck on the planet, but those who left survived to prosper on another planet.")
                    elif SQUEEZE_EVERYONE_INTO_SHIPS_OPTION == option:
                        print("Everyone squeezed into the ships and survived to land and colonize a planet, but everyone had to visit a chiropractor due to being squeezed into the ships.")
                    else:
                        # INDICATE THAT AN INVALID CHOICE WAS SELECTED.
                        print("Invalid choice!")
                elif GO_ALONG_WITH_PLAN_OPTION == option:
                    # DISPLAY THE RESULT OF THE PLAYER'S CHOICE.
                    print("You, your friend, and a few others escape, but those who disagreed remained on the planet.")
                else:
                    # INDICATE THAT AN INVALID CHOICE WAS SELECTED.
                    print("Invalid choice!")
            elif CONTINUE_WORKING_OPTION == option:
                # DISPLAY THE RESULT OF THE PLAYER'S CHOICE.
                print("You continue working, and a few days later, you learned that your friend has escaped.")
            else:
                # INDICATE THAT AN INVALID CHOICE WAS SELECTED.
                print("Invalid choice!")
        elif LEAVE_AND_GO_TO_BRIGHT_START_OPTION == option:
            # DISPLAY THE RESULT OF THE PLAYER'S CHOICE.
            print("You head toward the bright star.  It interferes with your ship's navigational systems, causing you to unexpectedly land on a nearby planet.")
        else:
            # INDICATE THAT AN INVALID CHOICE WAS SELECTED.
            print("Invalid choice!")
    elif LEAVE_NOW_OPTION == option:
        # DISPLAY THE RESULT OF THE PLAYER'S CHOICE.
        print('You leave the planet and safely return home.')
    else:
        # INDICATE THAT AN INVALID CHOICE WAS SELECTED.
        print("Invalid choice!")
elif STAY_INDOORS_OPTION == option:
    # DISPLAY THE RESULT OF THE PLAYER'S CHOICE.
    print("You stayed indoors.  The quake got worse, and you became unconscious...")
else:
    # INDICATE THAT AN INVALID CHOICE WAS SELECTED.
    print("Invalid choice!")

# END THE GAME.
print("Game Over")
print("Thank you for playing!")
print("Exiting game...")

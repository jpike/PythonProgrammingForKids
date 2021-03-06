# INTRODUCE PLAYERS TO THE GAME.
print("Welcome to Space Colony Adventure!")
print("To play, input a 1 to choose the 1st option or a 2 to choose the 2nd option.")
print("Beginning...")

# HAVE THE PLAYER MAKE A DECISION FOR THE FIRST SCENARIO.
print("You wake up one morning on a space colony on the moon of the planet Ewar.  You feel a quake and rumbles.")
print("Choose an option: ")
print("1. Run outside with your space suit on.")
print("2. Stay indoors.")
option = int(input("Input your option now (1 or 2): "))

# RESPOND TO THE OPTION THE PLAYER SELECTED FOR THE SCENARIO.
if 1 == option:
    # HAVE THE PLAYER MAKE A DECISION FOR THE NEXT SCENARIO.
    print("You run outdoors, get on a ship, and escape the planet.")
    print("You land on a planet that appears to be abandoned.")
    print("Choose an option: ")
    print("1. Stay there and leave in the morning after some rest.")
    print("2. Leave now.")
    option = int(input("Input your option now (1 or 2): "))

    # RESPOND TO THE OPTION THE PLAYER SELECTED FOR THE SCENARIO.
    if 1 == option:
        # HAVE THE PLAYER MAKE A DECISION FOR THE NEXT SCENARIO.
        print("During the night, you see a bright light and hear some rumbling.")
        print("Choose an option: ")
        print("1. Go outside to investigate.")
        print("2. Leave the planet and head towards a bright star.")
        option = int(input("Input your option now (1 or 2): "))

        # RESPOND TO THE OPTION THE PLAYER SELECTED FOR THE SCENARIO.
        if 1 == option:
            # HAVE THE PLAYER MAKE A DECISION FOR THE NEXT SCENARIO.
            print("You ran outside and were captured by aliens.")
            print("The aliens put you to work.  You see a friend motioning you over with his hand.")
            print("Choose an option: ")
            print("1. Go over and see what your friend wants.")
            print("2. Continue working.")
            option = int(input("Input your option now (1 or 2): "))

            # RESPOND TO THE OPTION THE PLAYER SELECTED FOR THE SCENARIO.
            if 1 == option:
                # HAVE THE PLAYER MAKE A DECISION FOR THE NEXT SCENARIO.
                print("You met up with your friend.  He came up with an escape plan.  You, your family, and friends debate on whether to follow the plan or not.  Some agree with the plan.  Others do not.")
                print("Choose an option: ")
                print("1. Continue debating.")
                print("2. Decide to go along with the plan with only you, your friend, and a few others.")
                option = int(input("Input your option now (1 or 2): "))

                # RESPOND TO THE OPTION THE PLAYER SELECTED FOR THE SCENARIO.
                if 1 == option:
                    # HAVE THE PLAYER MAKE A DECISION FOR THE NEXT SCENARIO.
                    print("Everyone reaches agreement with a new plan.  The plan is carried out.  However, near the end of the plan, you notice that you do not have enough escape ships to comfortably seat everyone.")
                    print("Choose an option: ")
                    print("1. Send others and stay behind yourself with a few others.")
                    print("2. Squeeze everyone into ships.")
                    option = int(input("Input your option now (1 or 2): "))

                    # RESPOND TO THE OPTION THE PLAYER SELECTED FOR THE SCENARIO.
                    if 1 == option:
                        print("You and a few others remain stuck on the planet, but those who left survived to prosper on another planet.")
                    elif 2 == option:
                        print("Everyone squeezed into the ships and survived to land and colonize a planet, but everyone had to visit a chiropractor due to being squeezed into the ships.")
                    else:
                        # INDICATE THAT AN INVALID CHOICE WAS SELECTED.
                        print("Invalid choice!")
                elif 2 == option:
                    # DISPLAY THE RESULT OF THE PLAYER'S CHOICE.
                    print("You, your friend, and a few others escape, but those who disagreed remained on the planet.")
                else:
                    # INDICATE THAT AN INVALID CHOICE WAS SELECTED.
                    print("Invalid choice!")
            elif 2 == option:
                # DISPLAY THE RESULT OF THE PLAYER'S CHOICE.
                print("You continue working, and a few days later, you learned that your friend has escaped.")
            else:
                # INDICATE THAT AN INVALID CHOICE WAS SELECTED.
                print("Invalid choice!")
        elif 2 == option:
            # DISPLAY THE RESULT OF THE PLAYER'S CHOICE.
            print("You head toward the bright star.  It interferes with your ship's navigational systems, causing you to unexpectedly land on a nearby planet.")
        else:
            # INDICATE THAT AN INVALID CHOICE WAS SELECTED.
            print("Invalid choice!")
    elif 2 == option:
        # DISPLAY THE RESULT OF THE PLAYER'S CHOICE.
        print('You leave the planet and safely return home.')
    else:
        # INDICATE THAT AN INVALID CHOICE WAS SELECTED.
        print("Invalid choice!")
elif 2 == option:
    # DISPLAY THE RESULT OF THE PLAYER'S CHOICE.
    print("You stayed indoors.  The quake got worse, and you became unconscious...")
else:
    # INDICATE THAT AN INVALID CHOICE WAS SELECTED.
    print("Invalid choice!")

# END THE GAME.
print("Game Over")
print("Thank you for playing!")
print("Exiting game...")

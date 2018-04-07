
def PrintBox(box_width_in_characters, box_height_in_characters):
    for row in range(box_height_in_characters):
        print("x" * box_width_in_characters)

box_width_in_characters = int(input("Enter box width: "))
box_height_in_characters = int(input("Enter box height: "))
PrintBox(box_width_in_characters, box_height_in_characters)

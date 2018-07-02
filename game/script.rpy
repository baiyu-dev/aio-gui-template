# The script of the game goes in this file.

# Declare characters used by this game. The color argument colorizes the
# name of the character.

define e = Character("Eileen")


# The game starts here.

label start:

    # Show a background. This uses a placeholder by default, but you can
    # add a file (named either "bg room.png" or "bg room.jpg") to the
    # images directory to show it.

    scene bg room

    # This shows a character sprite. A placeholder is used, but you can
    # replace it by adding a file named "eileen happy.png" to the images
    # directory.

    show eileen happy at center:
        yoffset 200

    # These display lines of dialogue.

    e "Lorem ipsum dolor sit amet, consectetur adipiscing elit. In ullamcorper porta ipsum sit amet sodales."

    e "Duis vehicula eros non massa vulputate iaculis. Nulla facilisi."

    "In urna sem, auctor volutpat ante id, aliquam ultricies augue. Integer eget molestie dolor."

    e "Sed lobortis diam urna, rhoncus lobortis odio condimentum eget. Etiam fermentum nibh dui, eget ullamcorper odio elementum eget."

    e "Etiam auctor maximus tellus, eget venenatis justo euismod at."

    e "Integer eget quam eu felis tempus volutpat. Donec et quam sit amet justo interdum feugiat. Suspendisse tempus id metus ac imperdiet."

    "Go ahead and click the History button in the quickmenu below to read the text history log!"
    
    # This ends the game.

    return

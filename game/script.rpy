# TO-DO: FIGURE OUT WHY renpy.count_dialogue_blocks() IS NOT WORKING PROPERLY

# The script of the game goes in this file.

# Declare characters used by this game. The color argument colorizes the
# name of the character.

define e = Character("Eileen", color="#f88787")
define e_nvl = Character("Eileen", color="#f88787", kind=nvl)
define nar_nvl = nvl_narrator

init python:

    ## This creates the End Credits portion.
    
    credits = ('Music', 'Eric Matyas'), ('Backgrounds', 'mugenjohncel'), ('Sprites', 'Mannequin by AR14'), ('Programming', 'BáiYù')
    credits_s = "{size=80}Credits\n\n"
    c1 = ''
    for c in credits:
        if not c1==c[0]:
            credits_s += "\n{size=40}" + c[0] + "\n"
        credits_s += "{size=60}" + c[1] + "\n"
        c1=c[0]
    credits_s += "\n\nMade with {a=https://www.renpy.org/}Ren'Py{/a} [renpy.version_only]."

    ## This creates a percentage based on how much of the game the player has seen.
    
    # numblocks = renpy.count_dialogue_blocks()
    # def percent():
    #     global result
    #     result = renpy.count_seen_dialogue_blocks()* 100 / numblocks

init:

    # Tracks how much of the game the player has seen.

    # default result = 0

    ## Image Displayables generated in-engine for use in the End Credits.

    # image cred = Text(credits_s, font="font.ttf", text_align=0.5) #use this if you want to use special fonts
    image cred = Text(credits_s, text_align=0.5)
    image theend = Text("{size=80}Fin", text_align=0.5)
    image thanks = Text("{size=80}Thanks for Playing!", text_align=0.5)
    #image game_results = Text("{size=80}You've seen [result]\% of the game.{/s}", text_align=0.5)
    #image devnote_unlock = Text("{size=80}You've unlocked a special message. Access it through the Extras Menu.", text_align=0.5)
    #image extras_unlock = Text("{size=80}You've unlocked the Extras Menu. Access it through the Main Menu.", text_align=0.5)

    ## Lets the engine know that this variable is False when the game is first played.
    define persistent.extras_unlocked = False

    ## We give the music files a short name so we can easily call them in the script.
    define audio.summer = "audio/Careless-Summer_Looping.mp3"
    define audio.office = "audio/Future-Business_v001.mp3"
    define audio.garden = "audio/Sculpture-Garden_Looping.mp3"
    define audio.concrete = "audio/The-Concrete-Bakes_Looping.mp3"

# The game starts here.

label start:

    # Show a background. This uses a placeholder by default, but you can
    # add a file (named either "bg room.png" or "bg room.jpg") to the
    # images directory to show it.

    scene room

    # This shows a character sprite. A placeholder is used, but you can
    # replace it by adding a file named "eileen happy.png" to the images
    # directory.

    show eileen happy at center:
        yoffset 200

    with fade

    # This plays music that plays at full volume after 2 seconds

    play music garden fadein 2.0

    # Makes [result] work.
    # $ percent()

    # These display lines of dialogue.

    e "You've created a new Ren'Py game."

    # This changes the sprite's expression

    show eileen neutral with dissolve

    e "Once you add a story, pictures, and music, you can release it to the world!"

    "Lorem ipsum dolor sit amet, consectetur adipiscing elit. In ullamcorper porta ipsum sit amet sodales."

    show eileen surprised with dissolve

    nar_nvl "Etiam auctor maximus tellus, eget venenatis justo euismod at."

    e_nvl "Integer eget quam eu felis tempus volutpat. Donec et quam sit amet justo interdum feugiat. Suspendisse tempus id metus ac imperdiet."

    nar_nvl "Maecenas sit amet sagittis ligula, eget bibendum sapien."

    nvl clear

    e_nvl "Aliquam faucibus ipsum congue velit volutpat pellentesque."

    e_nvl "In vestibulum quam nec mi sollicitudin ultricies at in nunc."

    nar_nvl "Maecenas convallis rhoncus tortor eu feugiat."

    nvl clear

    stop music fadeout 1.0

    ## This ends the replay mode segment. Doesn't affect normal gameplay.
    $ renpy.end_replay()

    menu:

        "Choice 1":

            ## This empty label is solely for replay mode purposes.

            label office:

                pass

            e "You selected Choice 1."

            $ persistent.c1_seen = True
            play music office fadein 2.0
            scene future_office
            show eileen angry at center:
                yoffset 200
            with fade

            e "Duis vehicula eros non massa vulputate iaculis. Nulla facilisi."

            "Sed lobortis diam urna, rhoncus lobortis odio condimentum eget. Etiam fermentum nibh dui, eget ullamcorper odio elementum eget."


        "Choice 2":

            label beach:

                pass

            e "You selected Choice 2."

            $ persistent.c2_seen = True
            play music summer fadein 2.0
            scene sort_of_beautiful_beach_day
            show eileen upset at center:
                yoffset 200
            with fade

            e "In urna sem, auctor volutpat ante id, aliquam ultricies augue. Integer eget molestie dolor."

            "Integer vehicula hendrerit metus, in laoreet arcu ornare a."

    "Nam ornare eleifend justo, in fermentum ante viverra ullamcorper."

    ## This ends the replay mode segment. Doesn't affect normal gameplay.
    $ renpy.end_replay()

label credits:
    
    # End Credits

    ## We hide the quickmenu for the End Credits so they don't appear at the bottom.
    $ show_quick_menu = False

    $ credits_speed = 20 # Scrolling speed in seconds
    scene black # Replace with a proper background if desired
    with dissolve
    show theend:
        yanchor 0.5 ypos 0.5
        xanchor 0.5 xpos 0.5
    with dissolve
    with Pause(0.5)
    hide theend with dissolve
    show cred at Move((0.5, 2.2), (0.5, 0.0), credits_speed, repeat=False, bounce=False, xanchor="center", yanchor="bottom")
    with Pause(credits_speed)
    show thanks:
        yanchor 0.5 ypos 0.5
        xanchor 0.5 xpos 0.5
    with dissolve
    with Pause(3)
    hide thanks with dissolve

    #centered "You've seen [result] of the game."

    if persistent.c1_seen and persistent.c2_seen:
    #if result == 100:

        centered "You've unlocked a special message. Access it through the Extras Menu."
        # show devnote_unlock with dissolve
        # with Pause(3)
        # hide devnote_unlock with dissolve

        $ persistent.game_clear = True

    if persistent.extras_unlocked:

        pass

    else:

        centered "You've unlocked the Extras Menu. Access it through the Main Menu."
        # show extras_unlock with dissolve
        # with Pause(3)
        # hide extras_unlock with dissolve

        $ persistent.extras_unlocked = True

    ## We re-enable the quickscreen as the credits are over.

    $ show_quick_menu = True

    # This ends the game.

    return

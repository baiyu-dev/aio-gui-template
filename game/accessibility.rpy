## Original file by npckc - https://npckc.site or https://npckc.itch.io
## Download at https://npckc.itch.io/caption-tool-for-renpy

## With an additional Screenshake setting by TheoMinute - https://twitter.com/theominute
## Download at https://minute.itch.io/renpy-accessibility

## Custom Screenshake Effects by BáiYù - https://tofurocks.itch.io
## Placed at the bottom of this file

## Last updated: 07-20-2022

################################################################################
## Caption Tool
################################################################################

# Hello! This is Caption Tool, a simple tool for adding image and sound captions to your Ren'Py game, made by npckc (https://npckc.site)!

# Lines that begin with TODO: are sections where you may be required to do something with the code, so you can Ctrl+F TODO: to make sure you haven't missed anything.

# TODO: Please copy this file (accessibility.rpy) to the "game" folder of your game. As well, please add the following textbutton to a screen somewhere, like the Preferences screen in your screens.rpy file.

# textbutton _("Accessibility") action ShowMenu("accessibility")
# TODO: Remove the # when pasting in the preferences screen. You can also use the code in the screens.rpy file of this tool instead.

# Once you've done that, you're OK! Just edit accessibility.rpy to work with your game (e.g., add your own sound captions, change the image caption character name if necessary).

# You can take a look at script.rpy for an example of the code.

# If you use this tool, I would appreciate it if you can credit npckc (https://npckc.site or https://npckc.itch.io) or the tool in some way, but it isn't required.

################################################################################
## Table of Contents
################################################################################

# C1: Initialisation
# C2: Crossfade Audio Code
# C3: Sound Captions
# C4: Image Captions
# C5: Accessibility Menu
# C6: Initialising Sound Captions for Translations
# C7: npckc Licence
# C8: Screenshake Toggle

################################################################################
## C1: Initialization
################################################################################

# This asks the user whether they want to use image or sound captions the first time they boot the game. It uses Ren'Py's splashscreen function - you can add your own splashscreen to this label as well.
init -1:
    default persistent.sound_captions = False
    default persistent.image_captions = False
    default self.voicing = False
    default persistent.screenshake = True


# label splashscreen:

#     scene black
#     if not persistent.caption:
#         menu:
#             "Do you want sound captions on? They describe music and sound effects in text.{fast}"
#             "On":
#                 $ persistent.sound_captions = True
#             "Off":
#                 pass
#         menu:
#             "Do you want image captions on? They describe game visuals in text.{fast}"
#             "On":
#                 $ persistent.image_captions = True
#             "Off":
#                 pass
#         "These options can be changed at any time in the menu.{fast}"
#         $ persistent.caption = True
#     return

################################################################################
## C2: Crossfade Audio Code
################################################################################

## TODO: Figure out how to get this to work with Audio Captions
# init python:
#     renpy.music.register_channel("music1", "music", loop=True)

#     def audio_crossFade(fadeTime, music):
#         oldChannel = None
#         newChannel = None
#         if renpy.music.get_playing(channel="music") is not None and renpy.music.get_playing(channel="music1") is None:
#             oldChannel = "music"
#             newChannel = "music1"
#         elif renpy.music.get_playing(channel="music") is None and renpy.music.get_playing(channel="music1") is not None:
#             oldChannel = "music1"
#             newChannel = "music"
#         elif renpy.music.get_playing(channel="music") is None and renpy.music.get_playing(channel="music1") is None:
#             oldChannel = None
#             newChannel = "music"
            
#         if oldChannel is not None:
#             renpy.music.stop(channel= oldChannel, fadeout=fadeTime)
            
#         if newChannel is not None:
#             renpy.music.play(music, channel=newChannel,fadein=fadeTime)


# label start:
# play music songone fadein 2.0
# "The game starts"
# "Switch the music"
# $ audio_crossFade(2.0, "songtwo")
# "Music is cross-fading now"
# "Lorem ipsum."

################################################################################
## C3: Sound Captions
################################################################################

# These are the commands for playing music and sounds, as well as where sound captions are defined. Please change the text to fit your own

init python:

# This is the text that will show whenever you play a sound. The sound description will follow.

    soundtext = _("Sound: ")

# This is the text that will show whenever you play music. The music description will follow.
    musictext = _("Music: ")

# This is where you define the names for the sound files you will be using in the game.

# TODO: Add your own sound files.

    # example = "audio/examplefile.ogg"
    door = "audio/sfx/Interior-Door_Close.mp3"
    drawer_close = "audio/sfx/Chest-Drawer_Close.mp3"
    drawer_open = "audio/sfx/Chest-Drawer_Open.mp3"
    ocean = "audio/sfx/Edge-of-Ocean.mp3"

# This is where you define the sound captions for each sound file you will be using in the game. Please make sure the names of the sounds defined above match the ones used for the captions below.

# TODO: Add your own sound captions.

    sound_list = {
    # example: _("Example text here"),
    door : _("A door closes"),
    drawer_close : _("A drawer closes"),
    drawer_open : _("A drawer opens"),
    ocean : _("Ocean waves hit the shore")
    }

# This is where you define the names for the music files you will be using in the game. It is recommended to define the main menu BGM as well.

# TODO: Add your own music files.

    # example = "audio/examplefile.ogg"
    business = "audio/music/Future-Business_v001.mp3"
    concrete = "audio/music/The-Concrete-Bakes_Looping.mp3"
    garden = "audio/music/Sculpture-Garden_Looping.mp3"
    summer = "audio/music/Careless-Summer_Looping.mp3"

# This is where you define the music captions for each music file you will be using in the game. Please make sure the names of the music defined above match the ones used for the captions below.

# TODO: Add your own music captions.

    music_list = {
    # example: _("Example text here"),
    business : _("Future Business"),
    concrete : _("The Concrete Bakes"),
    garden : _("Sculpture Garden"),
    summer : _("Careless Summer")
    }

# This is the sound command. It functions the same way as "play sound" normally does. You can change the fadein, fadeout and loop values when you invoke the command. If you do not change the values, the default values are 0.0 fadein, 0.0 fadeout, and no loop. If you change the values below, that will change the default values for every time you invoke the command.

    def play_sound(file, channel='sound', fadein=0.0, fadeout=0.0, loop=False, tight=None, relative_volume=1.0):
        renpy.sound.play(file, channel=channel, fadein=fadein, fadeout=fadeout, loop=loop, tight=tight, relative_volume=relative_volume)

        if persistent.sound_captions:
            renpy.notify(soundtext + sound_list[file])

# Here are some examples of how to use the play_sound command in your game.
# Put the name for the file that you defined above in the (brackets).
# Add additional values afterwards if you want to change them from the default.
#(Remove the # when using it.)

# $ play_sound(beepbeep)
# $ play_sound(phone, loop=True)

# You can also queue sounds with the queue command. It functions the same way as "queue sound" normally does. You can change the fadein, loop, clear_queue, tight, and relative_volume values when you invoke the command. If you do not change the values, the default values are 0.0 fadein, false for loop, true for clear_queue, none for tight, and 1.0 relative_volume. IF you change the values below, that will change the default values for every time you invoke the command.

    def queue_sound(file, channel='sound', fadein=0.0, loop=False, clear_queue=True, tight=None, relative_volume=1.0):
        renpy.sound.queue(file, channel=channel, fadein=fadein, loop=loop, clear_queue=clear_queue, tight=tight, relative_volume=relative_volume)

        if persistent.sound_captions:
            if type(file) is list:
                sound_queue = ""
                for i in range(len(file)):
                    sound_queue = sound_queue + sound_list[file[i]] + " / "
                sound_queue = sound_queue[:-3]
            else:
                sound_queue = sound_list[file]
            renpy.notify(soundtext + sound_queue)

# Here are some examples of how to use the queue_sound command in your game.
# Put the names for the files that you defined above in the (brackets) within [square brackets] and separated by a , comma.
# Add additional values afterwards if you want to change them from the default.
#(Remove the # when using it.)

# $ queue_sound([beepbeep, phone])
# $ queue_sound([phone, beepbeep], loop=True)

# You can use "stop sound" to stop the sound played from the play sound and queue sound commands, just as you would normally.

# This is the music command. It functions the same way as "play music" normally does. You can change the fadein, fadeout, loop, synchro_start, tight, if_changed, and relative_volume values when you invoke the command. If you do not change the values, the default values are 0.0 fadein, 0.0 fadeout, none for loop, false for synchro_start, none for tight, false for if_changed, and 1.0 relative_volume. If you change the values below, that will change the default values for every time you invoke the command.

    # def play_music(file, channel='music', fadein=0.0, fadeout=0.0):
    #     renpy.music.play(file, fadein=fadein, fadeout=fadeout)

    def play_music(file, channel='music', fadein=0.0, fadeout=0.0, loop=None, synchro_start=False, tight=None, if_changed=False, relative_volume=1.0):
        renpy.music.play(file, channel=channel, fadein=fadein, fadeout=fadeout, loop=loop, synchro_start=synchro_start, tight=tight, if_changed=if_changed, relative_volume=relative_volume)

        if persistent.sound_captions:
            renpy.notify (musictext + music_list[file])

# Here are some examples of how to use the play_music command in your game.
# Put the name for the file that you defined above in the (brackets).
# Add additional values afterwards if you want to change them from the default.
#(Remove the # when using it.)

# $ play_music(cake)
# $ play_music(cake,fadein=2.0,fadeout=2.0)

# You can also queue sounds with the queue command. It functions the same way as "queue sound" normally does. You can change the fadein, loop, clear_queue, tight, and relative_volume values when you invoke the command. If you do not chnage the values, the default values are 0.0 fadein, none for loop, true for clear_queue, none for tight, and 1.0 relative_volume. IF you change the values below, that will change the default values for every time you invoke the command.

    def queue_music(file, channel='music', fadein=0.0, loop=None, clear_queue=True, tight=None, relative_volume=1.0):
        renpy.music.queue(file, channel=channel, fadein=fadein, loop=loop, clear_queue=clear_queue, tight=tight, relative_volume=relative_volume)

        if persistent.sound_captions:
            if type(file) is list:
                music_queue = ""
                for i in range(len(file)):
                    music_queue = music_queue + music_list[file[i]] + " / "
                music_queue = music_queue[:-3]
            else:
                music_queue = music_list[file]
            renpy.notify(musictext + music_queue)

# Here are some examples of how to use the queue_music command in your game.
# Put the names for the files that you defined above in the (brackets) within [square brackets] and separated by a , comma.
# Add additional values afterwards if you want to change them from the default.
#(Remove the # when using it.)

# $ queue_music([title, hotsprings])
# $ queue_music([hotsprings, title], relative_volume=0.5)

# You can use "stop music" to stop the music played from the play music and queue music commands, just as you would normally.

# Note: By default, the play_sound command will play on the sound channel, and the play_music command will play on the music channel, but if you have custom channels, you can specify the channel in your command.

# Example:
# $ play_sound(ambientsound, channel='ambient')
# $ play_music(rainybgm, channel='weathermusic')

################################################################################
## C4: Image Captions
################################################################################

# This character, "ic", will speak if image captions or self-voicing is on. The default character name is None - that is, there is no name, like a narrator - but that can be changed.

define ic = Character(_(None),condition="persistent.image_captions or _preferences.self_voicing")

# Ren'Py also has "alt" (or "sv" in previous versions of Ren'Py), a built-in character that can be used for self-voicing. This character can be changed using config.descriptive_text_character, if you would like to use the \"alt\" character for something else.

# Example:
# define config.descriptive_text_character = "sv" << This would make the built-in self-voicing character "sv" instead, so you can use "alt" as a character elsewhere.

# You can read more about Ren'Py's built-in self-voicing options here: https://www.renpy.org/doc/html/self_voicing.html


################################################################################
## C5: Accessibility Menu
################################################################################

# This can be used if you want a menu ONLY for accessibility options. You can also copy and paste the buttons into the default Ren'Py preferences screen.

#### For this template, that's what we've done by default. ####

# screen accessibility():

#     tag menu

#     use game_menu(_("Preferences"), scroll="viewport"):
#         vbox:
#             style_prefix "check"
#             label _("Accessibility")
#             textbutton _("Sound Captions") action ToggleVariable("persistent.sound_captions")
#             textbutton _("Image Captions") action ToggleVariable("persistent.image_captions")
#             # Self-voicing does not work on smartphone devices, so this option only shows if the user is playing on a PC.
#             if renpy.variant("pc"):
#                 textbutton _("Self-Voicing") action Preference("self voicing", "toggle")
#             # This shows Ren'Py's built-in accessibility menu, added to Ren'Py in Ren'Py 7.2.2. This can also be displayed by pressing "A" on the keyboard when playing on a PC. As this option can break the way the game is displayed and also does not support translation as of Ren'Py build 7.3.2, you may want to hide the option. The button should also be removed if your version of Ren'Py is under 7.2.2, as the menu does not exist in previous versions.
#             textbutton _("More Options...") action Show("_accessibility")
#             textbutton ("") #Adds space between accessibility options and return button
#             # The Return button will return the user to the Preferences menu. It can be removed if it isn't necessary.

#             textbutton _("Return") action ShowMenu("preferences")

################################################################################
## C6: Initialising Sound Captions for Translations
################################################################################

# If you are translating your game, adding the following will make sure that sound captions are properly initialised when starting a new game or loading a save file.

# TODO: Add this to the beginning of your start label:

# $ renpy.change_language(_preferences.language, force=True)
# Remove the # when copying and pasting.

# You can see an example in script.rpy.

# TODO: If you are using the Ren'Py after_load label elsewhere, you can just include the code from here into your label

# label after_load:

#     $ renpy.change_language(_preferences.language, force=True)

#     return

# Please refer to script.rpy for an example of how to translate sound captions for a different language.

################################################################################
## C7: npckc Licence
################################################################################

# Copyright 2020 npckc

# Permission is hereby granted, free of charge, to any person obtaining a copy of this software and associated documentation files (the "Software"), to deal in the Software without restriction, including without limitation the rights to use, copy, modify, merge, publish, distribute, sublicense, and/or sell copies of the Software, and to permit persons to whom the Software is furnished to do so, subject to the following conditions:

# The above copyright notice and this permission notice shall be included in all copies or substantial portions of the Software.

# THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY, FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM, OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE SOFTWARE.

################################################################################
## C8: Screenshake
################################################################################

### Originally by TheoMinute

init python:
    # Shakes the screen. To use, put
    # $ shake()
    # inline. For other uses, simply do a check inline for ATL statements,
    ## or a ConditionSwitch for shaky images.

    def shake():

        if persistent.screenshake:

            # renpy.with_statement(hpunch)
            ## Uncomment the one above if you prefer the default screenshake
            renpy.with_statement(small_shake)


        else:

            renpy.with_statement(fade)
            ### OPTIONAL: Show a different effect if screenshake is turned off.

### Custom Screen Shake Effect by BáiYù

init:

    python:

        import math

        class Shaker(object):

            anchors = {
                'top' : 0.0,
                'center' : 0.5,
                'bottom' : 1.0,
                'left' : 0.0,
                'right' : 1.0,
                }

            def __init__(self, start, child, dist):
                if start is None:
                    start = child.get_placement()
                #
                self.start = [ self.anchors.get(i, i) for i in start ]  # central position
                self.dist = dist    # maximum distance, in pixels, from the starting point
                self.child = child

            def __call__(self, t, sizes):
                # Float to integer... turns floating point numbers to
                # integers.
                def fti(x, r):
                    if x is None:
                        x = 0
                    if isinstance(x, float):
                        return int(x * r)
                    else:
                        return x

                xpos, ypos, xanchor, yanchor = [ fti(a, b) for a, b in zip(self.start, sizes) ]

                xpos = xpos - xanchor
                ypos = ypos - yanchor

                nx = xpos + (1.0-t) * self.dist * (renpy.random.random()*2-1)
                ny = ypos + (1.0-t) * self.dist * (renpy.random.random()*2-1)

                return (int(nx), int(ny), 0, 0)

        def _Shake(start, time, child=None, dist=100.0, **properties):

            move = Shaker(start, child, dist=dist)

            return renpy.display.layout.Motion(move,
                          time,
                          child,
                          add_sizes=True,
                          **properties)

        Shake = renpy.curry(_Shake)

    $ small_shake = Shake((0, 0, 0, 0), 1.0, dist=10)
    $ short_shake = Shake((0, 0, 0, 0), 1.5, dist=15)
    $ med_shake = Shake((0, 0, 0, 0), 2, dist=20)
    $ long_shake = Shake((0, 0, 0, 0), 2.5, dist=25)
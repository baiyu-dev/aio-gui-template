## Original file by minute - https://twitter.com/minutekiwi
## Download at https://minute.itch.io/renpy-accessibility

## NOTE: THIS TEMPLATE USES THE AUDIO CAPTION FUNCTIONS IN captiontool.rpy
## ORIGINAL LINES FROM minute ARE COMMENTED OUT FOR REFERENCE

init python:
    ###Button Actions
    # These are the button actions found in screens replacements.rpy

    def changeFont(newFont):
        return SetField(persistent,"pref_text_font",newFont),SetField(persistent,"pref_text_size", size_dict[newFont][persistent.pref_text_scale]),SetField(persistent,"pref_text_spacing",size_dict[newFont]['line_spacing']),SelectedIf(persistent.pref_text_font == newFont)
        ###

    def changeScale(newScale):
        return SetField(persistent,"pref_text_scale",newScale),SetField(persistent,"pref_text_size", size_dict[persistent.pref_text_font][newScale])

    def changeColor(newColor):
        return SetField(persistent,"pref_text_color",newColor)

    #A quick way to toggle True/False on persistent variables.

    def persistentToggle(persistentfield):
        return ToggleField(persistent,persistentfield,true_value=True,false_value=False)

    # ### Audio Cues
    # # These are used in place of "play music" and "play sound". In your script:
    # # $ play_sfx(door_close)
    # # will play the door close sound effect.
    # # $ play_music(lamentoso,10)
    # # will play "lamentoso" with a 10 second fadein.

    # def play_sfx(sound_alias,fade=0):
    #   renpy.sound.play(sound_alias,fadein=fade)
    #   if persistent.audio_cues:
    #       renpy.notify("SFX: {i}" + sfx_dictionary[renpy.sound.get_playing('sound')] + "{/i}")

    # def play_music(music_alias,fade=0):
    #   renpy.music.play(music_alias,fadein=fade)
    #   if persistent.audio_cues:
    #       renpy.notify("Now Playing: " + music_dictionary[renpy.music.get_playing('music')])
    # ###

    ###Screenshake
    # Shakes the screen. To use, put
    # $ shake()
    # inline. For other uses, simply do a check inline for ATL statements, or a ConditionSwitch for shaky images.

    def shake():
        if persistent.screenshake:
            renpy.with_statement(hpunch)
        else:
            renpy.with_statement(fade) ###OPTIONAL: Show a different effect if screenshake is turned off.

define vt = Character(None,condition="persistent.visual_text_help or _preferences.self_voicing",what_italic=True)

###Image Description
# For users who are visually impaired or otherwise use self-voicing, many times it's useful to have additional
# on screen text to compensate for effects, subtle visual changes, etc. Ren'Py has a built in character, but
# since we want the ability to see the additional text *without* activating self-voicing, we have to make our own.
# Replace all instances of "sv" (The Character) in your script with "vt".

##Whether or not to display additional text for visual effects, etc
default persistent.visual_text_help = _preferences.self_voicing

###Initial GUI preferences
#Here, we'll keep all our gui preferences, along with our persistent variables regarding accessibility.

#Audio cues
default persistent.audio_cues = True

#Can we shake the screen/display shaking images?
default persistent.screenshake = True

##Default alpha of the say window. Append to your say screen.
default persistent.say_window_alpha = 0.75

#Used to determine what size font to use when changing font/size.
default persistent.pref_text_scale = "regular"

#Default spacing/kerning of say dialogue text. Append to your say screen.
default persistent.say_dialogue_kerning = 0

#Set your default font
#Replace all instances of gui.text_font with persistent.pref_text_font. Append to your say screen.
default persistent.pref_text_font = "gui/fonts/NotoSans-Regular.ttf"

#Set your default text size
#Replace all instances of gui.text_size with persistent.pref_text_size. Append to your say screen.
default persistent.pref_text_size = 32

#Default text color
#Replace all instances of gui.text_color with persistent.pref_text_color. Append to your say screen.
default persistent.pref_text_color = "#ffffff"

#Default line_spacing for your text.
#Append to to your say screen.
default persistent.pref_text_spacing = 0

###

###
#This is all the functions for accessibility.

init python:
    ###Size Dictionary
    # Organized in dicts, follow the order below to create your font:size pairings.
    # Since lots of fonts use different vertical heights, it's highly recommended you include a "line_spacing" key for
    # each entry.
    # For advanced usage, if you do a font size slider you can make these minimum and maximum sizes!

    size_dict = {
        # "filepath" : {"size_scale1" : size in pixels, "size_scale2" : size in pixels...},
        # For advanced usage, you can make these dicts hold any optional arguments you want per font.
        "gui/fonts/OpenDyslexic-Regular.otf" : {
            "regular" : 31,
            "large" : 35,
            "line_spacing" : -15,
            },

        "gui/fonts/NotoSans-Regular.ttf" : {
            "regular" : 31,
            "large" : 35,
            "line_spacing" : 0,
            },

        # DejaVuSans.ttf is the default font that ships with Ren'Py, so this is the only one
        # that won't be in the gui/fonts/ directory.
        "DejaVuSans.ttf" : {
            "regular" : 32,
            "large" : 35,
            "line_spacing" : 0,
            }#,

        # # This is a template for adding a different font option to the game, where 
        # # [font.ttf] is the name of your file.
        # "gui/fonts/[font.ttf]" : {
        #     "regular" : 32,
        #     "large" : 35,
        #     "line_spacing" : 0,
        #     },
        }


    # ###Initial Audio Cues Setup
    # # Define every song with an alias

    # # sad_song = "filepath.mp3"

    # # alias : "Song Title",
    # music_dictionary = {
    #     # sad_song : "Sad Song's Title",
    # }

    # # Define every sound with an alias
    # # door_close = "door closing sfx.wav"

    # # alias : "Sound description."
    # sfx_dictionary = {
    #     # door_close : "Door closes shut.",
    # }

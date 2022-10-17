## This is a resource name loader that will import the names of files from certain folders
## Intended as a way to quickly grab file names to use in accessibility.rpy and screens.rpy
## Remember to add commas to the end of each listed item
## As of RenPy7, basic images do not have to be defined (LayeredImages still need to be set up)
init -1:
    $ redefine_resources = False
    ## When you add, delete or rename an image or music resource, change redefine_resources to True and launch the project

## Sprites:
    # image eileen_base_casual = "images/sprites/eileen_base_casual.png"
    # image eileen_base_summer = "images/sprites/eileen_base_summer.png"
    # image eileen_face_angry = "images/sprites/eileen_face_angry.png"
    # image eileen_face_happy = "images/sprites/eileen_face_happy.png"
    # image eileen_face_neutral = "images/sprites/eileen_face_neutral.png"
    # image eileen_face_surprised = "images/sprites/eileen_face_surprised.png"
    # image eileen_face_upset = "images/sprites/eileen_face_upset.png"
    # image eileen_headband = "images/sprites/eileen_headband.png"
## BGs:
    # image future_office = "images/BG/future_office.jpg"
    # image room = "images/BG/room.jpg"
    # image sort_of_beautiful_beach_day = "images/BG/sort_of_beautiful_beach_day.jpg"
## CGs:

## Music:
# init -2 python:
    # Careless-Summer_Looping = "audio/music/Careless-Summer_Looping.mp3"
    # Future-Business_v001 = "audio/music/Future-Business_v001.mp3"
    # Sculpture-Garden_Looping = "audio/music/Sculpture-Garden_Looping.mp3"
    # The-Concrete-Bakes_Looping = "audio/music/The-Concrete-Bakes_Looping.mp3"

## Music Caption:
    # Careless-Summer_Looping: _("")
    # Future-Business_v001: _("")
    # Sculpture-Garden_Looping: _("")
    # The-Concrete-Bakes_Looping: _("")

## SFX:
    # Chest-Drawer_Close = "audio/sfx/Chest-Drawer_Close.mp3"
    # Chest-Drawer_Open = "audio/sfx/Chest-Drawer_Open.mp3"
    # Edge-of-Ocean = "audio/sfx/Edge-of-Ocean.mp3"
    # Interior-Door_Close = "audio/sfx/Interior-Door_Close.mp3"

## SFX Caption:
    # Chest-Drawer_Close: _("")
    # Chest-Drawer_Open: _("")
    # Edge-of-Ocean: _("")
    # Interior-Door_Close: _("")

## Script to redefine the images:
## !!! DO NOT CHANGE THE CODE BELOW THIS POINT !!!
init -1 python:

    if redefine_resources:
        with open(renpy.loader.transfn('definitions.rpy'), 'rb') as f:
            s = f.read()
        f.closed
        pos = s.find('## Script to redefine the images')
        if pos>1:
            s=s[pos:]

        with open(renpy.loader.transfn('definitions.rpy'), 'wb') as f:
            f.write('## This is a resource name loader that will import the names of files from certain folders\n## Intended as a way to quickly grab file names to use in accessibility.rpy and screens.rpy\n## Remember to add commas to the end of each listed item\n## As of RenPy7, basic images do not have to be defined (LayeredImages still need to be set up)\r\ninit -1:\r\n    $ redefine_resources = False\n    ## When you add, delete or rename an image or music resource, change redefine_resources to True and launch the project\r\n\r\n')

            f.write('## Sprites:\r\n')
            for file in renpy.list_files():
                if file.startswith('images/sprites') and (file.endswith('.png') or file.endswith('.webp')):
                    name = file.replace('images/sprites/','').replace('/', ' ').replace('.png','').replace('.webp','')
                    img_str = 'image ' + name + ' = "' + file + '"'
                    f.write('    # ' + img_str + '\r\n')

            f.write('## BGs:\r\n')
            for file in renpy.list_files():
                if file.startswith('images/BG/') and (file.endswith('.png') or file.endswith('.webp') or file.endswith('.jpg')):
                    name = file.replace('images/BG/','').replace('/', ' ').replace('.png','').replace('.webp','').replace('.jpg','')
                    img_str = 'image ' + name + ' = "' + file + '"'
                    f.write('    # ' + img_str + '\r\n')

            f.write('## CGs:\r\n')
            for file in renpy.list_files():
                if file.startswith('images/CG/') and (file.endswith('.png') or file.endswith('.webp') or file.endswith('.jpg')):
                    name = file.replace('images/CG/','').replace('/', ' ').replace('.png','').replace('.webp','').replace('.jpg','')
                    img_str = 'image ' + name + ' = "' + file + '"'
                    f.write('    # ' + img_str + '\r\n')
            
            f.write('\r\n## Music:\r\n# init -2 python:\r\n')
            for file in renpy.list_files():
                if file.startswith('audio/music/') and (file.endswith('.ogg') or file.endswith('.wav') or file.endswith('.mp3')):
                    name = file.replace('audio/music/','').replace('/', ' ').replace('.ogg','').replace('.wav','').replace('.mp3','')
                    my_str = name + ' = "' + file + '"'
                    f.write('    # ' + my_str + '\r\n')

            f.write('\r\n## Music Caption:\r\n')
            for file in renpy.list_files():
                if file.startswith('audio/music/') and (file.endswith('.ogg') or file.endswith('.wav') or file.endswith('.mp3')):
                    name = file.replace('audio/music/','').replace('/', ' ').replace('.ogg','').replace('.wav','').replace('.mp3','')
                    my_str = name + ' = "' + file + '"'
                    f.write('    # ' + name + ': _("")' + '\r\n')

            f.write('\r\n## SFX:\r\n')
            for file in renpy.list_files():
                if file.startswith('audio/sfx/') and (file.endswith('.ogg') or file.endswith('.wav') or file.endswith('.mp3')):
                    name = file.replace('audio/sfx/','').replace('/', ' ').replace(' ', '_').replace('.ogg','').replace('.wav','').replace('.mp3','')
                    my_str = name + ' = "' + file + '"'
                    f.write('    # ' + my_str + '\r\n')

            f.write('\r\n## SFX Caption:\r\n')
            for file in renpy.list_files():
                if file.startswith('audio/sfx/') and (file.endswith('.ogg') or file.endswith('.wav') or file.endswith('.mp3')):
                    name = file.replace('audio/sfx/','').replace('/', ' ').replace(' ', '_').replace('.ogg','').replace('.wav','').replace('.mp3','')
                    my_str = name + ' = "' + file + '"'
                    f.write('    # ' + name + ': _("")' + '\r\n')
            f.write('\r\n')
        f.closed
        
        with open(renpy.loader.transfn('definitions.rpy'), 'ab') as f:
            f.write(s)
        f.closed
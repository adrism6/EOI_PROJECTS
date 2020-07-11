from PIL import Image

# RESIZE IMAGE 'img' to new one with height 'baseheight' and proportional width
"""
baseheight = 1280
img = Image.open("./PewPewPew/img/main_menu.png")
wpercent = baseheight / float(img.size[1])
wsize = int((float(img.size[0]) * float(wpercent)))
img = img.resize((wsize, baseheight), Image.ANTIALIAS)
img.save("./PewPewPew/img/main_menu1.png")

"""
# RESIZE IMAGE 'img' to new one with width 'basewidth' and proportional height

basewidth = 1280
img = Image.open("./PewPewPew/img/new_weapon.png")
wpercent = basewidth / float(img.size[0])
hsize = int((float(img.size[1]) * float(wpercent)))
img = img.resize((basewidth, hsize), Image.ANTIALIAS)
img.save("./PewPewPew/img/new_weapon_menu.png")


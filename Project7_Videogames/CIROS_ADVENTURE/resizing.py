from PIL import Image

# RESIZE IMAGE 'img' to new one with height 'baseheight' and proportional width
"""
baseheight = 72
img = Image.open("./img/mobs/Hunter_King.png")
wpercent = baseheight / float(img.size[1])
wsize = int((float(img.size[0]) * float(wpercent)))
img = img.resize((wsize, baseheight), Image.ANTIALIAS)
img.save("./img/mobs/Hunter_King_res.png")
"""

# RESIZE IMAGE 'img' to new one with width 'basewidth' and proportional height

basewidth = 100
img = Image.open("./img/weapons/shotgun.png")
wpercent = basewidth / float(img.size[0])
hsize = int((float(img.size[1]) * float(wpercent)))
img = img.resize((basewidth, hsize), Image.ANTIALIAS)
img.save("./img/README_IMAGES/shotgun.png")


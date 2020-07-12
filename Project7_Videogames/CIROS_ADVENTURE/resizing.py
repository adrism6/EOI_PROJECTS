from PIL import Image

# RESIZE IMAGE 'img' to new one with height 'baseheight' and proportional width

baseheight = 70
img = Image.open("./path/to/file.png")
wpercent = baseheight / float(img.size[1])
wsize = int((float(img.size[0]) * float(wpercent)))
img = img.resize((wsize, baseheight), Image.ANTIALIAS)
img.save("./path/to/newfile.png")

# RESIZE IMAGE 'img' to new one with width 'basewidth' and proportional height
"""
basewidth = 140
img = Image.open("./path/to/file.png")
wpercent = basewidth / float(img.size[0])
hsize = int((float(img.size[1]) * float(wpercent)))
img = img.resize((basewidth, hsize), Image.ANTIALIAS)
img.save("./path/to/newfile.png")

"""


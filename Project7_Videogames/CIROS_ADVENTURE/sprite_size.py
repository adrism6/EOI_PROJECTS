from PIL import Image

image = Image.open("./img/bullets/sword.png")  # image to resize
new_image = image.resize((35, 15))  # size
new_image.save("./img/bullets/sword2.png")  # new archive


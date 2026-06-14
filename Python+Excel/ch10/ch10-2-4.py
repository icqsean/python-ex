from PIL import Image

im = Image.open("koala_small.png")
print(im.size)
im2 = im.rotate(45)
im2.save("koala_rotated01.jpg")
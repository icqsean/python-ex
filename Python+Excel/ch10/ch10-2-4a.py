from PIL import Image

im = Image.open("koala_small.png")
print(im.size)
im2 = im.transpose(Image.Transpose.ROTATE_90)
im2.save("koala_rotated02.jpg")
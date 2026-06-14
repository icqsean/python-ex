from PIL import Image

im = Image.open("koala.jpg")
print(im.size)
im2 = im.resize((400, 400))
print(im2.size)
im2.save("koala_resized01.jpg")

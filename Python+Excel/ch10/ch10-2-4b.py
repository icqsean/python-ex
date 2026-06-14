from PIL import Image

im = Image.open("koala.jpg")
print(im.size)
im2 = im.crop((50,100,300,400))
im2.save("koala_croped01.jpg")
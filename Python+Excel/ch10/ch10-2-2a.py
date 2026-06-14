from PIL import Image

im = Image.open("koala.jpg")
print(im.size)
new_width = 350
ratio = float(new_width)/im.width
new_height = int(im.height*ratio)
im2 = im.resize((new_width, new_height))
print(im2.size)
im2.save("koala_resized02.jpg")
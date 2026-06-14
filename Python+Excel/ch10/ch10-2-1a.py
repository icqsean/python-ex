from PIL import Image

im = Image.open("koala.jpg")
print(im.format, im.size, im.mode)
print("轉換輸出成PNG格式...")
im.save("koala.png")
print("轉換輸出成GIF格式...")
im.save("koala.gif", "GIF")

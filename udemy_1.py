from PIL import Image

mac = Image.open('images\\example.jpg')
print(type(mac))
mac.show()

mac.crop()
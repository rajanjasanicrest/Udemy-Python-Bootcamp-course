from PIL import Image

mac = Image.open('images\\word_matrix.png')
mac2 = Image.open('images\\mask.png')

mac2 = mac2.resize(mac.size)

mac2.putalpha(128)
mac.paste(im = mac2, box = (0,0), mask= mac2)
mac.show()

mac.save('images\\secret_msg.png')
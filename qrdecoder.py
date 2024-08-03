from pyzbar.pyzbar import decode
from PIL import Image

data = input("Enter the name of the image:")

img = Image.open(data)

results = decode(img)
print(results)

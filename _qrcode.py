import qrcode

data="I NEED TO TELL YOU SOMETHING, UNFORTUNATELY I CANT USE WHATSAPP FOR THIS. RUN!!!!!!!!!"


name = input("Name of QR Code:")
img = qrcode.make(data)
img.save(name+'.jpeg')


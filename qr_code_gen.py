import qrcode
from PIL import *

print("1. QR Code for Link\n2. OR Code for Text")
choice=int(input("Enter your choice(1-2)\t:"))
if choice==1:
    data=input("Enter Link\t:")
elif choice==2:
    data=input("Enter custom message\t:")
qr = qrcode.QRCode(
    version=1,
    error_correction=qrcode.constants.ERROR_CORRECT_M,
    box_size=10,
    border=5,
)
qr.add_data(data)
custom = input("Any color customization(Y/N)\t:")
if custom.lower()=='n':
    img = qr.make_image(fill_color="black", back_color="white")
else:
    fgc=input("Fill Color\t:")
    bgc=input("Back Color\t:")
    img = qr.make_image(fill_color=fgc,back_color=bgc)
type(img)  # qrcode.image.pil.PilImage
img.save("qr.png")
img = Image.open("qr.png")
img.show()


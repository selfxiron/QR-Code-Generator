import os
import qrcode

# vCard data
vCard_data = """
BEGIN:VCARD
VERSION:3.0
N:Jeet Pratap Singh; Rajput;;;
FN: Jeet Pratap Singh Rajput
TITLE: Mechanical Engineering Undergrad
TEL: +91 8770710960
EMAIL: selfxiron@gmail.com
URL: https://www.linkedin.com/in/jeet-pratap-singh-rajput/
END:CARD
"""


qr = qrcode.QRCode(
    version=1,
    error_correction=qrcode.constants.ERROR_CORRECT_L,
    box_size=10,
    border=2
)
qr.add_data(vCard_data)
qr.make(fit=True)
qr_image = qr.make_image(fill="black", back_color="white")
filename = input("Enter filename to save QR code (without extension): ") + ".png"
qr_image.save(filename)
print(f"QR Code saved as {filename}!")
os.system(filename)
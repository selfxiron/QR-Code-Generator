import os
import qrcode

# Ask user for QR code type
choice = input("Do you want to generate a QR code for your vCard? (yes/no): ").strip().lower()

if choice == "yes":
    # Read vCard data from file
    try:
        with open("vCard_data.txt", "r", encoding="utf-8") as file:
            data = file.read()
        filename = "vcard_qr.png"
    except FileNotFoundError:
        print("Error: vcard.txt file not found! Please create the file and add your vCard details.")
        exit(1)
else:
    # Get custom input from user
    data = input("Enter the text or URL to generate QR code: ").strip()
    filename = input("Enter filename to save QR code (without extension): ").strip() + ".png"

# Generate QR Code
qr = qrcode.QRCode(
    version=1,
    error_correction=qrcode.constants.ERROR_CORRECT_L,
    box_size=10,
    border=2
)
qr.add_data(data)
qr.make(fit=True)

# Save QR Code
qr_image = qr.make_image(fill="black", back_color="white")
qr_image.save(filename)

print(f"QR Code saved as {filename}!")
os.system(filename)  # Opens the QR code image automatically
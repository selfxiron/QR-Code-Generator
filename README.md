# 🎯 QR Code Generator
A simple and efficient **Python-based QR Code Generator** that allows users to convert text or URLs into QR codes and automatically open the generated QR code image.

## ✨ Features
- Generates QR codes for vCard contact details.
- Generate QR codes for any text or URL.
- Customizable filename for saving QR codes.
- Automatically detects the system and opens the generated QR code image.
- Simple and lightweight, requiring minimal dependencies.
- Handles missing vCard_data.txt gracefully with an error message.

## 📌 Installation Prerequisites
Make sure you have Python 3 installed on your system.

### 📦 Install Required Modules
Run the following command to install the required dependencies while being in the QR-Code-Generator directory:
```sh
pip install -r requirements.txt
```
Now the dependent external libraries will be installed.

## 🛠 Usage
Clone the repository and run the script:

```sh
git clone https://github.com/selfxiron/QR-Code-Generator
cd QR-Code-Generator
python qrgenerator.py
```

### Option 1: Generate QR Code for vCard
#### Note: You need to write/edit your details in vCard_data.txt file.
- The script will check for vCard_data.txt
- If found, it will generate a QR code containing vCard details.
- The QR Code will be saved as vCard_qr.png

### Option 2: Generate QR Code for Custom Text/URL
- The script will prompt for a text or URL.
- Users can enter any text (eg., "hello world") or URL (eg., "https://www.google.com/").
- It will ask for a filename and save the QR code with that name.
- Python will automatically detect the system and open the QR code saved by filename.

## 🔧 Technologies Used
- Python3
- qrcode module
- PIL (Pillow for image processing)
- OS module (for opening images automatically)

## 🚀 Future Enhancements
- GUI version using Tkinter or PyQt
- Option to generate colored QR codes
- QR Code scanner integration

## 📝 Notes
- Ensure that vCard_data.txt exists in the same directory as qrgenerator.py if using the vCard option.
- The script will automatically open the generated QR code image after saving.

## 🤝 Contributing
Feel free to fork this project and submit pull requests for improvements!

## 📜 License
This project is open-source and free to use.
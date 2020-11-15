from PIL import Image
import pytesseract
from pytesseract import image_to_string
import os

class ImagetoString:
    def getString(self,path):
        pytesseract.pytesseract.tesseract_cmd = r"C:\Program Files\Tesseract-OCR\tesseract.exe"
        secret = image_to_string(Image.open(path))
        os.remove('images/message.png')
        return secret

if __name__ == "__main__":
    i = ImagetoString()
    i.getString()
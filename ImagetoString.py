from PIL import Image
import pytesseract
from pytesseract import image_to_string

class ImagetoString:
    def getString(self,path):
        pytesseract.pytesseract.tesseract_cmd = r"C:\Program Files\Tesseract-OCR\tesseract.exe"
        print(image_to_string(Image.open(path)))
        return image_to_string(Image.open(path))

if __name__ == "__main__":
    i = ImagetoString()
    i.getString()
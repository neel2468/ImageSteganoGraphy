from PIL import Image, ImageDraw, ImageFont
import textwrap
from Crypto.Cipher import AES
import random
import string
import pytesseract
import cv2
from PIL import Image
import io

class Stego:
    original_image = {}
    original_image_width = 0
    original_image_height = 0
    encoded_message_image = {}
    stego_image = {}
    length = 0
    password_characters = ''

    def get_random_string(self,length):
        self.password_characters = string.ascii_letters + string.digits + string.punctuation
        self.key = ''.join(random.choice(self.password_characters) for i in range(length))
        print("Random string password is:", self.key)
        return self.key;
   
    def getOriginalImage(self): 
        self.original_image = Image.open('s2.png','r')
        self.original_image_width = self.original_image.width
        self.original_image_height = self.original_image.height

    def getMsgFromUser(self):
        secret_message = input("Enter secret message \n")
        self.generate_encoded_image_from_text(secret_message)
        print(type(secret_message))
        key = self.get_random_string(16)
        obj = AES.new(key.encode("utf8"), AES.MODE_CFB, 'This is an IV456'.encode("utf8"))
        ciphertext = obj.encrypt(secret_message.encode("utf8"))
        print(ciphertext)
        self.encoded_message_image = self.generate_encoded_image_from_text(ciphertext)
       
        
        

    def generate_encoded_image_from_text(self,text):
        image_text = Image.new('1',(self.original_image_width,self.original_image_height),1)
        font = ImageFont.truetype("times.ttf", 15)

        drawer = ImageDraw.Draw(image_text)

        margin = offset = 10
        for line in textwrap.wrap(str(text), width=60):
            drawer.text((margin,offset), line, font=font)
            offset += 10

        return image_text

    def hide(self):
        self.stego_image = Image.new('RGB',(self.original_image_width,self.original_image_height))
        for x in range(self.original_image_width):
            for y in range(self.original_image_height):
                coord = x,y
                red = self.original_image.getpixel(coord)[0]
                green = self.original_image.getpixel(coord)[1]
                blue = self.original_image.getpixel(coord)[2]
                
                if self.encoded_message_image.getpixel(coord) == 0:
                    self.stego_image.putpixel(coord,((red+1),green,blue))
                else:
                    self.stego_image.putpixel(coord,(red,green,blue))

        self.stego_image.save('o1.png')

    
    def unhide(self):
       
        
        output_image = Image.open('o1.png','r')
        decoded_msg_image = Image.new('1',(self.original_image_width,self.original_image_height),255)
        for x in range(self.original_image_width):
            for y in range(self.original_image_height):
                coord = x,y
                red = output_image.getpixel(coord)[0]
                if red - self.original_image.getpixel(coord)[0] > 0:
                    decoded_msg_image.putpixel(coord,0)
                else:
                    decoded_msg_image.putpixel(coord,1)
        
        print(decoded_msg_image)
        print(type(decoded_msg_image))
       
        decoded_msg_image.save('message.bmp')
     #   self.image_to_byte_array(decoded_msg_image);
     #   print(type(decoded_msg_image))
        
    def image_to_byte_array(self,image:Image):
      imgByteArr = io.BytesIO()
      print(image.format)
      image.save(imgByteArr, format=image.format)
      imgByteArr = imgByteArr.getvalue()
      print(imgByteArr)
      return imgByteArr




s1 = Stego()
s1.getOriginalImage()
s1.getMsgFromUser()
s1.hide()
s1.unhide()


        





    
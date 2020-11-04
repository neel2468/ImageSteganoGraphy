from PIL import Image, ImageDraw, ImageFont
import io

import textwrap

class Stego:
    original_image = {}
    original_image_width = 0
    original_image_height = 0
    encoded_message_image = {}
    stego_image = {}
    length = 0
    password_characters = ''

    def getOriginalImage(self,path):
        self.original_image = Image.open(path,'r')
        self.original_image_width = self.original_image.width
        self.original_image_height = self.original_image.height


    def getMsgFromUser(self):
        secret_message = input("Enter secret message \n")
        self.generate_encoded_image_from_text(secret_message)




    def generate_encoded_image_from_text(self,text):
        image_text = Image.new('RGB',(self.original_image_width,self.original_image_height),color=(255,255,255))
        drawer = ImageDraw.Draw(image_text)
        font = ImageFont.truetype("mono.ttf",24)
        margin = offset = 30
        for line in textwrap.wrap(text, width=85):
            drawer.text((margin,offset), line,font=font, align="center",spacing=10,fill=(0,0,0))
            offset += 30

        image_text.save('images/hidden.png')
        return image_text

    def hide(self):
        self.stego_image = Image.new('RGB',(self.original_image_width,self.original_image_height))
        for x in range(self.original_image_width):
            for y in range(self.original_image_height):
                coord = x,y
                red = self.original_image.getpixel(coord)[0]
                green = self.original_image.getpixel(coord)[1]
                blue = self.original_image.getpixel(coord)[2]

                if self.encoded_message_image.getpixel(coord)[0] == 0:
                    if red == 0:
                        red = red + 1
                        self.stego_image.putpixel(coord,(red,green,blue))
                    else:
                        red = red - 1
                        self.stego_image.putpixel(coord,(red,green,blue))
                else:
                    self.stego_image.putpixel(coord,(red,green,blue))

        self.stego_image.save('images/o1.png')


    def unhide(self,originalPath, stegoPath):


        output_image = Image.open(stegoPath,'r')
        original_image = Image.open(originalPath,'r')
        decoded_msg_image = Image.new('RGB',(original_image.width,original_image.height))
        for x in range(self.original_image_width):
            for y in range(self.original_image_height):
                coord = x,y
                red = output_image.getpixel(coord)[0]
                if red - self.original_image.getpixel(coord)[0] == 1 or self.original_image.getpixel(coord)[0] - red == 1:
                    decoded_msg_image.putpixel(coord,(0,0,0))
                else:
                    decoded_msg_image.putpixel(coord,(255,255,255))

        decoded_msg_image.save('images/message.png')

    def image_to_byte_array(self,image:Image):
      imgByteArr = io.BytesIO()
      image.save(imgByteArr, format=image.format)
      imgByteArr = imgByteArr.getvalue()
      return imgByteArr

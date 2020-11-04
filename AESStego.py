from Crypto.Cipher import AES
from PIL import Image
import random
import string
class AESStego:

    def get_random_string(self,length):
        self.password_characters = string.ascii_letters + string.digits + string.punctuation
        self.key = ''.join(random.choice(self.password_characters) for i in range(length))
        return self.key;

# Convert encoding data into 8-bit binary
# form using ASCII value of characters
    def genData(self,data):

            # list of binary codes
            # of given data
            newd = []
            for i in data:
                newd.append(format(ord(b'%c' % i ), '08b'))
            return newd

    # Pixels are modified according to the
    # 8-bit binary data and finally returned
    def modPix(self,pix, data):

        datalist = self.genData(data)
        lendata = len(datalist)
        imdata = iter(pix)

        for i in range(lendata):

            # Extracting 3 pixels at a time
            pix = [value for value in imdata.__next__()[:3] +
                                    imdata.__next__()[:3] +
                                    imdata.__next__()[:3]]

            # Pixel value should be made
            # odd for 1 and even for 0
            for j in range(0, 8):
                if (datalist[i][j] == '0' and pix[j]% 2 != 0):
                    pix[j] -= 1

                elif (datalist[i][j] == '1' and pix[j] % 2 == 0):
                    if(pix[j] != 0):
                        pix[j] -= 1
                    else:
                        pix[j] += 1
                    # pix[j] -= 1

            # Eighth pixel of every set tells
            # whether to stop ot read further.
            # 0 means keep reading; 1 means thec
            # message is over.
            if (i == lendata - 1):
                if (pix[-1] % 2 == 0):
                    if(pix[-1] != 0):
                        pix[-1] -= 1
                    else:
                        pix[-1] += 1

            else:
                if (pix[-1] % 2 != 0):
                    pix[-1] -= 1

            pix = tuple(pix)
            yield pix[0:3]
            yield pix[3:6]
            yield pix[6:9]

    def encode_enc(self,newimg, data):
        w = newimg.size[0]
        (x, y) = (0, 0)

        for pixel in self.modPix(newimg.getdata(), data):

            # Putting modified pixels in the new image
            newimg.putpixel((x, y), pixel)
            if (x == w - 1):
                x = 0
                y += 1
            else:
                x += 1

    # Encode data into image
    def encode(self,data,datakey,path):
        image = Image.open(path, 'r')
        obj = AES.new(datakey.encode("utf8"), AES.MODE_CFB, 'This is an IV456'.encode("utf8"))
        data = obj.encrypt(data.encode("utf8"))
        if (len(data) == 0):
            raise ValueError('Data is empty')

        newimg = image.copy()
        self.encode_enc(newimg, data)

        newimg.save("images/aes.png", str("images/aes.png".split(".")[1].upper()))
        return data

    # Decode the data in the image
    def decode(self,key,path):

        image = Image.open(path, 'r')

        data = b'';
        imgdata = iter(image.getdata())

        while (True):
            pixels = [value for value in imgdata.__next__()[:3] +
                                    imgdata.__next__()[:3] +
                                    imgdata.__next__()[:3]]

            # string of binary data
            binstr = ''

            for i in pixels[:8]:
                if (i % 2 == 0):
                    binstr += '0'
                else:
                    binstr += '1'

            data = b"".join([data, int(binstr, 2).to_bytes(1, byteorder='big')])
            if (pixels[-1] % 2 != 0):

                obj2 = AES.new(key.encode("utf8"), AES.MODE_CFB, 'This is an IV456'.encode("utf8"))
                plaintext = obj2.decrypt(data)
                return plaintext.decode("utf-8")

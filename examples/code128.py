#-*- encoding: utf-8 -*-
"""Example code for code128 library"""


import logging
import sys
from hubarcode.code128 import Code128Encoder
from PIL import Image,ImageDraw,ImageFont

#logging.getLogger("code128").setLevel(logging.DEBUG)
#logging.getLogger("code128").addHandler(logging.StreamHandler(sys.stdout))

'''
使用huBarcode,pygame和PIL生成条形码
'''


class StudentIDEnCoder:
    """encode student id as code128"""

    def __init__(self, id, name, grade, _class):
        """ * id: 
            * name:
            * grade:
            * class: """

        self.id = id
        self.name = name
        self.grade = grade
        self._class = _class
        self.option = {"ttf_font":"C:/Windows/Fonts/cambriab.ttf","ttf_fontsize":16, "up_border" : 30, "bottom_border":15,"height":120,"label_border":4}
        self.image = None

    def get_encode_image(self):
    	self.image = Code128Encoder(id.upper(), self.option).get_pilimage(bar_width=2)
    	imgw, imgh = self.image.size
    	ttf_fontsize = self.option.get('ttf_fontsize')
    	up_border = self.option.get('up_border')
    	print "up_border : ", up_border

    	im = Image.new('L', (imgw, imgh + up_border+1), 'white')
    	box = (0, up_border, imgw, up_border + imgh)
    	im.paste(self.image, box)

    	draw = ImageDraw.Draw(im)
    	#font = ImageFont.truetype(self.option.get('ttf_font'), self.option.get('ttf_fontsize'))
    	#draw.setfont(font)
    	font = ImageFont.truetype('simsun.ttc', ttf_fontsize, encoding="utf-8");
    	draw.text((2 * 10, up_border - ttf_fontsize), self.name, 'black', font=font)

    	class_info = str(self.grade) + u' 年级 ' + str(self._class) + u' 班 '
    	draw.text(( imgw / 2 , up_border - ttf_fontsize), class_info, 'black', font=font)



    	return im






if __name__ == "__main__":
    #1 生成条形码
    _id = sys.argv[1].upper()
    _name = sys.argv[2]
    file_name = _id + '.png'

    id = _id;
    name = unicode(_name, 'GBK')
    grade = 3
    _class = 2

    encoder = StudentIDEnCoder(id, name, grade, _class)
    img = encoder.get_encode_image()
    img.save(file_name, 'PNG')


'''
    encoder = Code128Encoder(text,options={"ttf_font":"C:/Windows/Fonts/cambriab.ttf","ttf_fontsize":14,
  "bottom_border":10,"height":100,"label_border":2})
    #encoder.save("test.png",bar_width=1)
    img = encoder.get_pilimage(bar_width=2)
    #img.save("tt.png", "PNG")
    img.save(file_name, 'PNG')
'''

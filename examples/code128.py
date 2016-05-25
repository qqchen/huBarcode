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



if __name__ == "__main__":
    #1 生成条形码
    text = sys.argv[1].upper()
    file_name = sys.argv[2]
    if file_name.find('png') < 0:
    	print 'wrong name'
    	exit(0)

    encoder = Code128Encoder(text,options={"ttf_font":"C:/Windows/Fonts/cambriab.ttf","ttf_fontsize":14,
  "bottom_border":10,"height":100,"label_border":2})
    #encoder.save("test.png",bar_width=1)
    img = encoder.get_pilimage(bar_width=2)
    #img.save("tt.png", "PNG")
    img.save(file_name, 'PNG')
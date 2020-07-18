# -*- coding: utf-8 -*-
"""
Created on Sat Jul 18 18:12:59 2020

@author: VARUN SAKUNIA
"""

from PIL import Image,ImageFont, ImageDraw

image = Image.open(r'D:\My_Face_DataSet\poster13.jpg')
draw = ImageDraw.Draw(image)

food = Image.open(r'D:\My_Face_DataSet\burger.jpg')
size = (250,250)
food1 = food.resize(size)


Image.Image.paste(image, food1, (60,350)) 

font = ImageFont.truetype("D:\My_Face_DataSet\hatmiwhitedafont.ttf", 130)
draw.text((50, 50), "Lightening Deal", font=font,fill='yellow')
# 
# 
font = ImageFont.truetype("D:\My_Face_DataSet\pineapple slice.ttf", 100)
draw.text((60, 230), "....Grab Soon....", font=font,fill='skyblue')
#
font = ImageFont.truetype("D:\My_Face_DataSet\salted caramel.ttf", 70)
draw.text((350, 350), "Cheese" + "\n"+" Burger", font=font,fill='red')
# 
font = ImageFont.truetype("D:\My_Face_DataSet\lambodia.ttf", 120)
draw.text((50, 600), "Just At 120/-", font=font,fill='orange')
# 
font = ImageFont.truetype("D:\My_Face_DataSet\hansley.otf", 60)
draw.text((30, 750), "Download our APP" +"\n"+ "To get more Awesome offers", font=font,fill='lightgreen')
# 
# 
# =============================================================================
image.show()
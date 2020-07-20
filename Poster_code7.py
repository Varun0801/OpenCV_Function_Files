# -*- coding: utf-8 -*-
"""
Created on Sun Jul 19 23:32:38 2020

@author: VARUN SAKUNIA
"""


from PIL import Image,ImageFont, ImageDraw

image = Image.open(r'D:\My_Face_DataSet\r1.jpg')
draw = ImageDraw.Draw(image)

food = Image.open(r'D:\My_Face_DataSet\pizza.jpg')
size = (400,400)
food1 = food.resize(size)


Image.Image.paste(image, food1, (175,325)) 

font = ImageFont.truetype("D:\My_Face_DataSet\gimme danger.ttf", 90)
draw.text((90, 100), "Most Awaiting", font=font,fill='darkgreen')
# 
# 
font = ImageFont.truetype("D:\My_Face_DataSet\c u d d l e s s p a c e d.ttf", 80)
draw.text((375, 260), "..Grab Soon..", font=font,fill='blue')
#
font = ImageFont.truetype("D:\My_Face_DataSet\hatmiwhitedafont.ttf", 120)
draw.text((600, 400), "Cheese Burst Pizza", font=font,fill='red')
# 
font = ImageFont.truetype("D:\My_Face_DataSet\garamond medium italic.ttf", 95)
draw.text((600, 600), "Only At 200/-", font=font,fill='orange')
# 
font = ImageFont.truetype("D:\My_Face_DataSet\marthiya.ttf", 35)
draw.text((470, 725), "Contact: 096178 83305"+"\n" + "Web: anshul@nanniz.com" +"\n"+"    Download our APP", font=font,fill='black')
# 
# =============================================================================
image.show()
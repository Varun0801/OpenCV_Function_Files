# -*- coding: utf-8 -*-
"""
Created on Sat Jul 18 17:13:45 2020

@author: VARUN SAKUNIA
"""

from PIL import Image,ImageFont, ImageDraw

image = Image.open(r'D:\My_Face_DataSet\poster3.jpg')
draw = ImageDraw.Draw(image)

food = Image.open(r'D:\My_Face_DataSet\burger.jpg')
size = (300,300)
food1 = food.resize(size)


Image.Image.paste(image, food1, (120,450)) 

font = ImageFont.truetype("D:\My_Face_DataSet\dayland.ttf", 100)
draw.text((250, 330), "Lightening Deal", font=font,fill='purple')
# 

font = ImageFont.truetype("D:\My_Face_DataSet\marthiya.ttf", 55)
draw.text((420, 440), "Delicious Burger", font=font,fill='red')
# 
font = ImageFont.truetype("D:\My_Face_DataSet\samberia.ttf", 90)
draw.text((450, 550), "Only At 120/-", font=font,fill='darkorange')
# 
# 
font = ImageFont.truetype("D:\My_Face_DataSet\sarllina.ttf", 100)
draw.text((110, 750), "Limited Time Offer", font=font,fill='blue')
#
font = ImageFont.truetype("D:\My_Face_DataSet\jakarta night - free personal use.ttf", 120)
draw.text((70, 900), "Contact us: 096178 83305"+"\n" + "Web: anshul@nanniz.com" +"\n"+"Download our APP", font=font,fill='darkgreen')
# 
# 
# =============================================================================
image.show()
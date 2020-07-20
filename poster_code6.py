# -*- coding: utf-8 -*-
"""
Created on Sun Jul 19 23:31:24 2020

@author: VARUN SAKUNIA
"""


from PIL import Image,ImageFont, ImageDraw

image = Image.open(r'D:\My_Face_DataSet\poster15.jpg')
draw = ImageDraw.Draw(image)

food = Image.open(r'D:\My_Face_DataSet\pizza1.jpg')
size = (275,275)
food1 = food.resize(size)


Image.Image.paste(image, food1, (175,325)) 

font = ImageFont.truetype("D:\My_Face_DataSet\krinkesdecorpersonal.ttf", 110)
draw.text((115, 100), "Offerss..", font=font,fill='darkorange')
# 
# 
font = ImageFont.truetype("D:\My_Face_DataSet\pineapple slice.ttf", 80)
draw.text((95, 230), "....Grab Soon....", font=font,fill='skyblue')
#
font = ImageFont.truetype("D:\My_Face_DataSet\pixel-spyder-2-0.ttf", 90)
draw.text((185, 500), "Pizza", font=font,fill='blue')
# 
font = ImageFont.truetype("D:\My_Face_DataSet\hey august.otf", 95)
draw.text((90, 600), "Only At 200/-", font=font,fill='orange')
# 
font = ImageFont.truetype("D:\My_Face_DataSet\design.collection2.toontiei.ttf", 30)
draw.text((85, 725), "Contact: 096178 83305"+"\n" + "Web: anshul@nanniz.com" +"\n"+"    Download our APP", font=font,fill='red')
# 
# 
# =============================================================================
image.show()
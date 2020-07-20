# -*- coding: utf-8 -*-
"""
Created on Sun Jul 19 18:46:43 2020

@author: VARUN SAKUNIA
"""


from PIL import Image,ImageFont, ImageDraw

image = Image.open(r'D:\My_Face_DataSet\poster16.jpg')
draw = ImageDraw.Draw(image)

food = Image.open(r'D:\My_Face_DataSet\pizza.jpg')
size = (290,290)
food1 = food.resize(size)


Image.Image.paste(image, food1, (175,325)) 

font = ImageFont.truetype("D:\My_Face_DataSet\krinkesdecorpersonal.ttf", 110)
draw.text((115, 120), "Offerss..", font=font,fill='red')
# 
# 
font = ImageFont.truetype("D:\My_Face_DataSet\shaumy.otf", 80)
draw.text((95, 240), "..Grab Soon..", font=font,fill='skyblue')
#
font = ImageFont.truetype("D:\My_Face_DataSet\stencil intellecta trash free.otf", 90)
draw.text((240, 530), "Pizza", font=font,fill='blue')
# 
font = ImageFont.truetype("D:\My_Face_DataSet\hey august.otf", 95)
draw.text((95, 600), "Only At 200/-", font=font,fill='white')
# 
font = ImageFont.truetype("D:\My_Face_DataSet\design.collection2.toontiei.ttf", 32)
draw.text((89, 725), "Contact: 096178 83305"+"\n" + "Web: anshul@nanniz.com" +"\n"+"    Download our APP", font=font,fill='black')
# 
# 
# =============================================================================
image.show()
# -*- coding: utf-8 -*-
"""
Created on Mon Jul 13 19:46:13 2020

@author: VARUN SAKUNIA
"""

from PIL import Image,ImageFont, ImageDraw
import cv2

image = Image.open(r'D:\My_Face_DataSet\poster12.jpg')
draw = ImageDraw.Draw(image)

font = ImageFont.truetype("D:\My_Face_DataSet\drifttyp.ttf", 45)
draw.text((330, 60), "Exciting" + "\n" + "Offers" + "\n" +"Awaiting..", font=font,fill='black')

font = ImageFont.truetype("D:\My_Face_DataSet\krinkesdecorpersonal.ttf", 65)
draw.text((55, 300), "Get The Best Deals", font=font,fill='red')

font = ImageFont.truetype("D:\My_Face_DataSet\glaser_becker_stencil.ttf", 50)
draw.text((50, 375), "Burger Now At 120/-", font=font,fill='orange')
font = ImageFont.truetype("D:\My_Face_DataSet\pixel-spyder.ttf", 100)
draw.text((55, 630), "Exclusively" + "\n"+"    with us", font=font,fill='red')
font = ImageFont.truetype("D:\My_Face_DataSet\AGFOR28.ttf", 40)
draw.text((50, 775), "Contact us:"+ "\n"+ "096178 83305"+"\n" + "Web: anshul@nanniz.com" +"\n"+"Download our APP", font=font,fill='black')

image.show()

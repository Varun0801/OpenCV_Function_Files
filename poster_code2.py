
from PIL import Image,ImageFont, ImageDraw

image = Image.open(r'D:\My_Face_DataSet\poster2.jpg')
draw = ImageDraw.Draw(image)

food = Image.open(r'D:\My_Face_DataSet\burger.jpg')
size = (150,150)
food1 = food.resize(size)


Image.Image.paste(image, food1, (260, 290)) 

# 
font = ImageFont.truetype("D:\My_Face_DataSet\pixel-spyder-2-0.ttf", 45)
draw.text((110, 600), "Limited Time Offer", font=font,fill='blue')

font = ImageFont.truetype("D:\My_Face_DataSet\samberia.ttf", 45)
draw.text((110, 520), "______Onlyyy At 120/-______", font=font,fill='darkorange')
# 
font = ImageFont.truetype("D:\My_Face_DataSet\LittleLordFontleroyNF.otf", 45)
draw.text((290, 440), "Burger", font=font,fill='red')
# 
font = ImageFont.truetype("D:\My_Face_DataSet\marchell.ttf", 45)
draw.text((120, 445), "Lightening Deal", font=font,fill="purple")
# 
font = ImageFont.truetype("D:\My_Face_DataSet\Lilybud.ttf", 55)
draw.text((160, 650), "Contact us: 096178 83305"+"\n" + "Web: anshul@nanniz.com" +"\n"+"Download our APP", font=font,fill='green')
# 
# 
# =============================================================================
image.show()
from PIL import Image,ImageDraw, ImageFont
from PIL.ImageFilter import SHARPEN
import numpy as np
# from tkinter import *


# window = Tk()
# window.geometry("500x500")


de_citizen = Image.open("personalausweis.png")
foto = "bill.png"
de_id = "A123902"
de_name = "ZORLU"
de_vorname = "MURAT"
de_day ='11'
de_gebort="Ankara"
de_sign = "signa.png"



pic = Image.open(foto).resize((220,290))
pic = pic.filter(SHARPEN)
de_citizen.paste(pic,(30,70))
signature  = Image.open('output.png').resize((90,60))

de_citizen.paste(signature,(300,310))

draw = ImageDraw.Draw(de_citizen)
font = ImageFont.truetype('OcrB2.ttf', size=25)
font2 = ImageFont.truetype('OCRB.otf', size=18)



draw.text((420,25), de_id,font=font,fill='black')
draw.text((272,60), de_name,font=font2,fill='black')
draw.text((272,120), de_vorname,font=font2,fill='black')
draw.text((272,170), de_day,font=font2,fill='black')
draw.text((310,170), de_day,font=font2,fill='black')
draw.text((272,215), de_gebort,font=font2,fill='black')
de_citizen.show()



# img = Image.open('signa.png')
# img = img.convert("RGBA")
# datas = img.getdata()
# newData = []
# for item in datas:
#     if item[0] == 255 and item[1] == 255 and item[2] == 255:
#         newData.append((255, 255, 255, 0))
#     else:
#         newData.append(item)

# img.putdata(newData)
# img.save("img2.png", "PNG")
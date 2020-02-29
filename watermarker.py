import glob
from PIL import Image, ImageDraw, ImageFont
from tkinter import filedialog

watermark = "©2020 connected2christ.com"
watermark_color = "white"
file_list = []


def change_watermark():
    """Update the watermark from the default or something else"""
    return input("Type in your new watermark: ")


def change_color():
    """Select a new color by user input"""
    return input("Choose a new color: ")


def select_files():
    """Select all files to watermark"""
    grabber = filedialog.askopenfilenames()
    return grabber


print("Defaults - Watermark: ", watermark, "Color: ",
      watermark_color, " \nMake any changes?")

check = input("Y/N: ")
if check == 'y' or check == 'Y':
    watermark = input("Enter new watermark: ")
    watermark_color = input("Enter color: ")

for pick in select_files(): #Get selected files, append to list
    file_list.append(pick)


font = ImageFont.truetype("arial.ttf", 12)
text_width, text_height = font.getsize(watermark) #determine size of watermark for placement

for pic in file_list:
    this_pic = Image.open(pic) #set variable as opened image
    pic_width = this_pic.width #detmine picture width
    pic_height = this_pic.height #and height
    draw = ImageDraw.Draw(this_pic) 
    draw.text((pic_width - text_width - 10, pic_height -
               text_height - 5), watermark, font=font, fill=watermark_color) #draw text on bottom right, with some extra room for a buffer
    this_pic.save(pic) #save over original image with watermark

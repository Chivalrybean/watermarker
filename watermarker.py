from PIL import Image, ImageDraw, ImageFont
from tkinter import filedialog

watermark = "©2020 connected2christ.com"
watermark_color = "white"
file_list = []


def change_watermark():
    """Update the watermark from the default or something else"""
    return input("Type in your new watermark: ")


def change_color():
    return input("Choose a new color: ")


def select_files():
    grabber = filedialog.askopenfilenames()
    return grabber


def new_height(width, height):
    aspect_ratio = width / height
    return 612 / aspect_ratio


print("Defaults - Watermark: ", watermark, "Color: ",
      watermark_color, " \nMake any changes?")

check = input("Y/N: ")
if check == 'y' or check == 'Y':
    watermark = input("Enter new watermark: ")
    watermark_color = input("Enter color: ")
else:
    pass

for pick in select_files():
    file_list.append(pick)


font = ImageFont.truetype("arial.ttf", 12)
text_width, text_height = font.getsize(watermark)

for pic in file_list:
    print(watermark)
    this_pic = Image.open(pic)
    if this_pic.width > 612:
        this_pic = this_pic.resize(
            (612, int(new_height(this_pic.width, this_pic.height))))
    draw = ImageDraw.Draw(this_pic)
    draw.text((this_pic.width - text_width - 10, this_pic.height -
               text_height - 5), watermark, font=font, fill=watermark_color)
    this_pic.save(pic)

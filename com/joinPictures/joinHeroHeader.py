##encoding = "utf-8"

import math
import PIL.Image as Image
import os

#打开拼接画板
def joinPictures():
    ls = os.listdir('D:/heroavatar')
    each_size = int(math.sqrt(float(640*640)/len(ls)))#每个图像的面积像素
    lines = int(640/each_size)#每个图像的边长像素
    image = Image.new('RGBA', (640, 640))
    x = 0
    y = 0
    for i in range(0,len(ls)):
        try:
            img = Image.open('./heroavatar'+'/'+ls[i])
        except IOError:
            print("Error")
        else:
            img = img.resize((each_size, each_size), Image.ANTIALIAS)
            image.paste(img, (x * each_size, y * each_size))
            x += 1
            if x == lines:
                x = 0
                y += 1
    image.save('./heroavatar' + "/" + "all.png")

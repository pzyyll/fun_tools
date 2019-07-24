""" 一个制作替换头像背景颜色的小工具(可以自制证件照～)
resetbg.py img_file color[blue|red|white]
"""

import sys
import removebg

from removebg import RemoveBg
from PIL import Image

class Color(object):
    BLUE = (30, 144, 255)
    RED = (255, 48, 48)
    WHITE = (255, 255, 255)

    @staticmethod
    def getColor(color):
        return {
            'blue': Color.BLUE,
            'red': Color.RED
        }.get(color, Color.BLUE)

API_KEY = 'ZE4zpXPftPoPsx4XoRcBSw46'

rmbg = RemoveBg(API_KEY, 'err.log')

jpg = sys.argv[1]
color = sys.argv[2]

rmbg.remove_background_from_img_file(jpg)

rawpng_path = jpg + '_no_bg.png'

rawpng = Image.open(rawpng_path)

x, y = rawpng.size
p = Image.new('RGBA', rawpng.size, Color.getColor(color))
p.paste(rawpng, (0, 0, x, y), rawpng)
p.save(jpg + '_' + color + '.png')

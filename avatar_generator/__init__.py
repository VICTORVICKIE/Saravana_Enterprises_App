from __future__ import (unicode_literals, absolute_import,
                        division, print_function)

import os
from random import randint, seed
from io import BytesIO
from PIL import Image, ImageDraw, ImageFont

__all__ = ['Avatar']


class Avatar(object):
    FONT_COLOR = (255, 255, 255)
    MIN_RENDER_SIZE = 512

    @classmethod
    def generate(cls, size, string, filetype="JPEG"):
    
        bg_base_color = (255,255,255)
        render_size = max(size, Avatar.MIN_RENDER_SIZE)
        image = Image.new('RGB', (render_size, render_size), bg_base_color)
        draw = ImageDraw.Draw(image)
        draw.ellipse((0, 0) + (render_size,render_size), fill=cls._background_color(string))
        font = cls._font(render_size)
        text = cls._text(string)
        draw.text(cls._text_position(render_size, text, font),
                  text,
                  fill=cls.FONT_COLOR,
                  font=font)
        stream = BytesIO()
        image = image.resize((size, size), Image.ANTIALIAS)
        image.save(stream, format=filetype, optimize=True)
        return stream.getvalue()

    @staticmethod
    def _background_color(s):
        
        seed(s)
        r = v = b = 255
        while r + v + b > 255*2:
            r = randint(0, 255)
            v = randint(0, 255)
            b = randint(0, 255)
        return (r, v, b)

    @staticmethod
    def _font(size):
       
        path = os.path.join(os.path.dirname(__file__), 'data',
                            "Inconsolata.otf")
        return ImageFont.truetype(path, size=int(0.8 * size))

    @staticmethod
    def _text(string):
        
        if len(string) == 0:
            return "#"
        else:
            return string[0].upper()

    @staticmethod
    def _text_position(size, text, font):
       
        width, height = font.getsize(text)
        left = (size - width) / 2.0
        top = (size - height) / 5.5
        return left, top

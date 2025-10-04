from PIL import Image
from turtle import *
speed(2000)

image = Image.open('experience/Billie-Eilish-Emblem-64.png')
rgb_im = image.convert('RGB')

size = image.width

setup(size*10,size*10)

def carre(n):
    """
    La fonction carre() crée un carré de côté 'n'
    n -> Taille du côté
    """
    for i in range(4):
        fd(n)
        lt(90)

colormode(255)

for i in range(size):
    for j in range(size):
        r,g,b = rgb_im.getpixel((i,j))
        r = int(r)
        g = int(g)
        b = int(b)
        color((r,g,b))
        up()
        goto(i*10-320,320-j*10)
        down()
        fillcolor((r,g,b))
        begin_fill()
        carre(10)
        end_fill()
getscreen().save("output1")

mainloop()
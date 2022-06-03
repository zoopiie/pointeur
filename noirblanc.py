from PIL import Image
from time import sleep

r = 30
g = 63
b = 63
def testcolor(x, y, w, h):
    color = 0

    img = Image.open('init.png')
    imgGray = img.convert('L')
    imgGray.save('test_gray.png')

    im = Image.open('test_gray.png') # Can be many different formats.
    pix = im.load()

    if pix[x, y] < r:
        color += 1

    if pix[x + w, y] < r:
        color += 1

    if pix[x, y + h] < r:
        color += 1

    if pix[x + w, y + h] < r:
        color += 1


    if color != 0:
        print("tu es dans le noir")
    else:
        print("dommage t'es dans le blanc")
    print("haut gauche : {} \n haut droite : {} \n bas gauche : {} \n bas droite : {}".format(pix[x, y],
                                                                                              pix[x + w, y],
                                                                                              pix[x, y + h],
                                                                                              pix[x + w, y + h]))

    sleep(1)


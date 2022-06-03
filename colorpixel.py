from PIL import Image
from time import sleep
import cv2

grey = 35
r = 71
g = 75
b = 93
def testcolor(x, y, w, h, iamge):
    color = 0

    im = Image.open(iamge) # Can be many different formats.
    pix = im.load()

    if pix[x, y][0] < r and pix[x, y][1] < 120 and pix[x, y][2] < b:
        color += 1

    if pix[x + w, y][0] < r and pix[x + w, y][1] < 120 and pix[x + w, y][2] < b:
        color += 1

    if pix[x, y + h][0] < r and pix[x, y + h][1] < 120 and pix[x, y + h][2] < b:
        color += 1

    if pix[x + w, y + h][0] < r and pix[x + w, y + h][1] < 120 and pix[x + w, y + h][2] < b:
        color += 1
    if color > 1:
        print("tu es dans le noir")
        print("haut gauche : {} \n haut droite : {} \n bas gauche : {} \n bas droite : {}".format(pix[x, y],
                                                                                                  pix[x + w, y],
                                                                                                  pix[x, y + h],
                                                                                                  pix[x + w, y + h]))
        return 1
    else:
        print("dommage t'es dans le blanc")
        print("haut gauche : {} \n haut droite : {} \n bas gauche : {} \n bas droite : {}".format(pix[x, y],
                                                                                                  pix[x + w, y],
                                                                                                  pix[x, y + h],
                                                                                                  pix[x + w, y + h]))
        return 0




def testgrey(x, y, w, h):
    color = 0

    img = Image.open('init.png')
    imgGray = img.convert('L')
    imgGray.save('test_gray.png')

    im = Image.open('test_gray.png')  # Can be many different formats.
    pix = im.load()

    if pix[x, y] < grey:
        color += 1

    if pix[x + w, y] < grey:
        color += 1

    if pix[x, y + h] < grey:
        color += 1

    if pix[x + w, y + h] < grey:
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

def testonepoint(x, y, w, h, iamge):
    color = 0

    im = Image.open(iamge) # Can be many different formats.
    pix = im.load()


    if pix[x + w/2, y + h/2][0] < r and pix[x + w/2, y + h/2][1] < g and pix[x + w/2, y + h/2][2] < b:
        print("tu es dans le noir")
    else:
        print("dommage t'es dans le blanc")
    print("centre du truc  {} ".format(pix[x + w/2, y + h/2]))

    img = cv2.imread(iamge)

    im = cv2.circle(img, (int(x + w/2), int(y + h/2)), 3, (0, 255, 0), thickness=1, lineType=8, shift=0)

    cv2.imwrite("image_test_cercle.png", im)


def testred(x, y, w, h, iamge):
    color = 0

    im = Image.open(iamge) # Can be many different formats.
    pix = im.load()


    if pix[x + w/2, y + h/2][0] > 140 and pix[x + w/2, y + h/2][1] < 98 and pix[x + w/2, y + h/2][2] < 98:
        print("tu es dans le noir")

        return 1
    else:
        print("dommage t'es dans le blanc")

        return 0



def testwhite(x, y, w, h, iamge):
    color = 0

    im = Image.open(iamge) # Can be many different formats.
    pix = im.load()

    rouge = pix[x + w/2, y + h/2][0]

    vert = pix[x + w/2, y + h/2][1]

    bleu = pix[x + w/2, y + h/2][2]

    blanc = rouge + vert + bleu

    ratio = blanc / 3 / rouge
    print(rouge, vert, bleu)
    print(ratio)

    if rouge > 110 and vert > 110 and bleu > 110 and 0.9 > ratio > 1.1:
        print("tu es dans le blanc")

        return 1
    else:
        print("c'est pas blanc en tout cas")

        return 0



def testonepoint2(x, y, w, h, iamge):
    color = 0

    im = Image.open(iamge) # Can be many different formats.
    pix = im.load()


    if pix[x + w/2, y + h/2][0] < r and pix[x + w/2, y + h/2][1] < g + 50 and pix[x + w/2, y + h/2][2] < b:
        print("centre du truc  {} ".format(pix[x + w / 2, y + h / 2]))
        return 1
    else:
        print("centre du truc  {} ".format(pix[x + w / 2, y + h / 2]))
        return 0



def testuncolor(x, y, w, h, iamge):
    color = 0
    rb, gb, bb = 110, 110, 110
    im = Image.open(iamge) # Can be many different formats.
    pix = im.load()

    if pix[x, y][0] > rb and pix[x, y][1] > gb and pix[x, y][2] > bb\
            and 0.9 < (pix[x, y][0] + pix[x, y][1] + pix[x, y][2]) / 3 / pix[x, y][0] < 1:
        color += 1

    if pix[x + w, y][0] > rb and pix[x + w, y][1] > gb and pix[x + w, y][2] > bb\
            and 0.9 < (pix[x + w, y][0] + pix[x + w, y][1] + pix[x + w, y][2]) / 3 / pix[x + w, y][0] < 1:
        color += 1

    if pix[x, y + h][0] > rb and pix[x, y + h][1] > gb and pix[x, y + h][2] > bb\
            and 0.9 < (pix[x, y + h][0] + pix[x, y + h][1] + pix[x, y + h][2]) / 3 / pix[x, y + h][0] < 1:
        color += 1

    if pix[x + w, y + h][0] > rb and pix[x + w, y + h][1] > gb and pix[x + w, y + h][2] > bb\
            and 0.9 < (pix[x + w, y + h][0] + pix[x + w, y + h][1] + pix[x + w, y + h][2]) / 3 / pix[x + w, y + h][0] < 1:
        color += 1
    if color > 1:
        print("c'est blanc")
        print("haut gauche : {} \n haut droite : {} \n bas gauche : {} \n bas droite : {}".format(pix[x, y],
                                                                                                  pix[x + w, y],
                                                                                                  pix[x, y + h],
                                                                                                  pix[x + w, y + h]))
        return 1
    else:
        print("t'es pas dans le blanc toi")
        print("haut gauche : {} \n haut droite : {} \n bas gauche : {} \n bas droite : {}".format(pix[x, y],
                                                                                                  pix[x + w, y],
                                                                                                  pix[x, y + h],
                                                                                                  pix[x + w, y + h]))
        return 0
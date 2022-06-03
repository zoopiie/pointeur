from PIL import Image


def tabl(image):
    im = Image.open(image)
    widht, height = im.size
    pix = im.load()
    tab = []
    r = 70
    g = 70
    b = 70
    for i in range (height):
        tab.append([])
        for j in range (widht):
            if pix[j, i][0] < r and pix[j, i][1] < g and pix[j, i][2] < b:
                tab[i].append(1)
            else:
                tab[i].append(0)
    return tab


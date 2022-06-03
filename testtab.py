

def test(x, y, w, h, tab):
    color = 0
    for j in range(y, y + h, 1):
        for i in range (x, x + w, 1):
            if tab[j][i] == 1:
                color += 1




    if color != 0:
        print('tu es dans le noir')
    else:
        print('tu es dans le blanc')


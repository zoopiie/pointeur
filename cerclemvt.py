from tkinter import *
import random
from time import sleep
from PIL import Image, ImageTk



temps = 100
x, xx, y, yy = 0, 200, 0, 200
old = 1
varmvt = 20
point = 0
def truc():
    global x, xx, y, yy, old
    f = open('toucher.txt', 'r')
    t = f.readlines()
    touch = int(t[0])
    f.close()

    if touch == 1:
        can.delete("cir")
        #button.config(text="cible suivante")
        sleep(3)
    else:
        dir = random.randint(0, 4)
        print(dir)

        if dir == 1 and old != 2 and xx < 1390:
            can.delete("cir")
            x += varmvt
            xx += varmvt
            can.create_oval(x, y, xx, yy, fill='black', tags="cir")
            old = 1

        if dir == 2 and old != 1 and x >= 10:
            can.delete("cir")
            x -= varmvt
            xx -= varmvt
            can.create_oval(x, y, xx, yy, fill='black', tags="cir")
            old = 2

        if dir == 3 and old != 4 and yy < 740:
            can.delete("cir")
            y += varmvt
            yy += varmvt
            can.create_oval(x, y, xx, yy, fill='black', tags="cir")
            old = 3

        if dir == 4 and old != 3 and y >= 10:
            can.delete("cir")
            y -= varmvt
            yy -= varmvt
            can.create_oval(x, y, xx, yy, fill='black', tags="cir")
            old = 4

    root.after(25, truc)

def truc2():
    global x, xx, y, yy, dir, old, point
    f = open('toucher.txt', 'r')
    t = f.readlines()
    touch = int(t[0])
    f.close()

    if touch == 0:
        point += 1
        can.delete("chat")
         #button.config(text="ton score est de {}".format(point))
        sleep(0.5)
        f = open('toucher.txt', 'w+')
        f.write(str(1))
        f.close()
        new_x = random.randint(0, 1050)
        new_y = random.randint(0, 650)

        x, xx, y, yy = new_x, new_x + 200, new_y, new_y + 200
    else:

        dir = old
        if dir == 1:
            if yy > 850 + varmvt + 1:
                old = 2

            if xx > 1200 + varmvt + 1:
                old = 3
            y += varmvt
            yy += varmvt
            x += varmvt
            xx += varmvt
            #can.delete("cir")
            #can.create_oval(x, y, xx, yy, fill='black', tags="cir")
            can.delete('chat')
            can.create_image(x, y, image=chat, tags="chat")


        if dir == 2:
            if y < 100 + varmvt - 1:
                old = 1

            if xx > 1250 + varmvt + 1:
                old = 4
            y -= varmvt
            yy -= varmvt
            x += varmvt
            xx += varmvt
            #can.delete("cir")
            #can.create_oval(x, y, xx, yy, fill='black', tags="cir")
            can.delete('chat')
            can.create_image(x, y, image=chat, tags="chat")

        if dir == 3:
            if yy > 850 + varmvt + 1:
                old = 4

            if x < 100 + varmvt - 1:
                old = 1
            y += varmvt
            yy += varmvt
            x -= varmvt
            xx -= varmvt
            #can.delete("cir")
            #can.create_oval(x, y, xx, yy, fill='black', tags="cir")
            can.delete('chat')
            can.create_image(x, y, image=chat, tags="chat")

        if dir == 4:
            if y < 100 + varmvt - 1:
                old = 3

            if x < 100 + varmvt - 1:
                old = 2
            y -= varmvt
            yy -= varmvt
            x -= varmvt
            xx -= varmvt
            #can.delete("cir")
            #can.create_oval(x, y, xx, yy, fill='black', tags="cir")
            can.delete('chat')
            can.create_image(x, y, image=chat, tags="chat")

    root.after(temps, truc2)


root = Tk()
root.geometry('1550x800')
root.config(bg="white")

chat = PhotoImage(file='cible.png')

"""button = Button(root, text="ton score est de {}".format(point), bg='#ffffff', fg='black', command=(temps - 10))
button.pack()"""

can = Canvas(root, width=1250, height=850, bg='#ffffff')
can.pack(expand=YES)

cari = 0
echec = 120
"""for j in range(0, (int(850/echec) + 1), 1):
    if cari == 0:
        cari = 1
    else:
        cari = 0
    for i in range(0, (int(1200/echec) + 1), 2):
        if cari == 0:
            can.create_rectangle(echec + i * echec, 0 + j * echec, echec * 2 + i * echec, echec + j * echec, fill='black')
        if cari == 1:
            can.create_rectangle(0 + i * echec, 0 + j * echec, echec + i * echec, echec + j * echec, fill='black')"""


#can.create_oval(x, y, xx, yy, fill='black', tags="cir")
#can.create_image(x, y, image=chat, tags="chat")

truc2()

root.mainloop()

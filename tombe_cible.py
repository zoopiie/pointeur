from tkinter import *

lst = [1,1,1,1]
lst_circle = [[0,0,100,100], [100,300, 200, 400], [300,600, 400, 700], [500,500, 600, 600]]


def test():
    truc = int(input('choisir un cercle a enlever : '))
    sting = "circle{}".format(truc)
    can.delete(sting)
    lst[truc-1] = 0
    var = lst[0] + lst[1] + lst[2] + lst[3]
    ouah = 0
    can.delete('all')
    for i in range (4):
        if lst[i]==1:
            ouah += 1

            can.create_oval(lst_circle[i][0], lst_circle[i][1], lst_circle[i][2], lst_circle[i][3],
                            fill='red',tags='circle{}'.format(ouah))





root = Tk()

root.geometry("1000x1000")
root['bg']='black'

can = Canvas(root, height=1000, width=1000, bg='black')
can.pack()

can.create_oval(0,0, 100, 100, fill='red', tags='circle1')
can.create_oval(100,300, 200, 400, fill='red', tags='circle2')
can.create_oval(300,600, 400, 700, fill='red', tags='circle3')
can.create_oval(500,500, 600, 600, fill='red', tags='circle4')


test()


root.mainloop()
from tkinter import *
from PIL import Image

def recupcolor():
    im = Image.open('image_test.png')  # Can be many different formats.
    pix = im.load()
    x = int(entryx.get())
    y = int(entryy.get())

    print(pix[x, y])



root = Tk()
root.config(bg='#00ffdd')
root.geometry("800x800")


"""label1 = Label(root, text="ceci est pour le couleur rouge", bg="#00ffdd", font=35, fg="black").pack(expand=YES)
entryrmax = Entry(root, text="ceci est pour le max couleur rouge", width=100)
entryrmax.pack(expand=YES)

label1 = Label(root, text="ceci est pour le couleur verte", bg="#00ffdd", font=35, fg="black").pack(expand=YES)
entrygmax = Entry(root, text="ceci est pour le max couleur verte", width=100)
entrygmax.pack(expand=YES)

label1 = Label(root, text="ceci est pour le couleur bleu", bg="#00ffdd", font=35, fg="black").pack(expand=YES)
entrybmax = Entry(root, text="ceci est pour le max couleur bleu", width=100)
entrybmax.pack(expand=YES)"""

label1 = Label(root, text="ceci est pour x", bg="#00ffdd", font=35, fg="black").pack()
entryx = Entry(root, text="ceci est pour le min couleur rouge", width=100)
entryx.pack()

label1 = Label(root, text="ceci est pour y", bg="#00ffdd", font=35, fg="black").pack()
entryy = Entry(root, text="ceci est pour le min couleur verte", width=100)
entryy.pack()

but = Button(root, text='print la couleur de la coordonnée', command=recupcolor).pack()


root.mainloop()
from tkinter import *
from random import randrange


# definition des fonctions gestionnaires d'evenements 
def drawline():
    """ Trace d'une ligne dans le canvas """
    print("trace d'une nouvelle ligne")
    global x1, y1, x2, y2, couleur
    can1.create_oval(x1, y1, x2, y2, width=2, fill=couleur)

    # modification des coordonnées pour la ligne suivante
    y2, y1 = y2+10, y1-10

def drawline2():
    """ Trace un viseur """
    can1.create_line(200, 325, 300, 325, width=2, fill='red')
    can1.create_line(250, 275, 250, 375, width=2, fill='red')

def changecolor():
    """ Changement aleatoire de la couleur du trace """
    global couleur
    pal = ['purple', 'cyan', 'maroon', 'green', 'blue', 'orange', 'yellow']
    c = randrange(len(pal))
    couleur = pal[c]
    print("la nouvelle couleur est:", couleur)

# Programme principal

""" variable globale """
x1, y1, x2, y2 = 0, 650, 500, 0
couleur = 'dark green'

# Creation widget principal
fen1 = Tk()
# Creation du widget esclave
can1 = Canvas(fen1, bg='dark grey', height=650, width=500)
can1.pack(side=LEFT)
bout1 = Button(fen1, text='Quitter', command=fen1.quit)
bout1.pack(side=BOTTOM)
bout2 = Button(fen1, text='Tracer une ligne', command=drawline)
bout2.pack()
bout3 = Button(fen1, text='Autre couleur', command=changecolor)
bout3.pack()
bout4 = Button(fen1, text='Viseur', command=drawline2)
bout4.pack()
# demarrage du receptionnaire d'evenement
fen1.mainloop()
# fermeture de la fenetre
fen1.destroy()



#-------------------------------------------------------------------------------
# Name:        Launcher
# Purpose:     Pues lanzar el juego ¿no sabes ingles o que?
#
# Author:      Mance... Alguien
#
# Created:     9/19/1999
# Copyright:   (c) COVID19 2020
# Licence:     <uranus>
#-------------------------------------------------------------------------------

import Game
import gc, math
from functools import partial
from Tipos import *
from tkinter import *
from PIL import Image, ImageTk

tips = [tip.name for tip in TiposPersonajes]
launcher = Tk()

def Execute(pers: str):
    launcher.destroy()
    Game.main(SELECT_PLAYER = pers)

launcher.title("(Perdiste)ElJuego.exe")
launcher.resizable(0, 0)
launcher.iconbitmap("Sprites/Utilidades/icon.ico")
launcher.config(bg="#202020")
launcher.config(relief="groove")
launcher.config(cursor="cross")
fondo = Image.open("Sprites/Utilidades/Inicio.png")
ancho,alto=800,600
fondo = fondo.resize((ancho, alto), Image.ANTIALIAS)
fondo = ImageTk.PhotoImage(fondo)
launcher.geometry("%dx%d+%d+%d" % (ancho, alto, (launcher.winfo_screenmmwidth()//2), (launcher.winfo_screenheight()//2)-(alto//2)))
lineas = math.ceil(len(tips)/5)
contenedor = Label(launcher, width = ancho, height = alto - int(100*lineas), image = fondo)
contenedor.pack(side=TOP, fill=X)
imas = [PhotoImage(file="Sprites/Personajes/%s/D0.gif" % i.capitalize()) for i in tips]
for i in range(lineas):
    menu = Frame(launcher, width=ancho,height=100)
    menu.pack()
    menu.config(bg="#202020")
    for j in range(5):
        if int((5*(i))+j) < len(tips):
            btn=Button(menu, text = tips[(5*(i))+j], command=partial(Execute, tips[(5*(i))+j]), width = int(ancho/5), height = 100, image = imas[(5*(i))+j])
            btn.pack(side=LEFT)

def main():
    launcher.mainloop()
    pass

if __name__ == '__main__':
    main()

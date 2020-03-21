#-------------------------------------------------------------------------------
# Name:        module1
# Purpose:
#
# Author:      estudiantes
#
# Created:     25/02/2020
# Copyright:   (c) estudiantes 2020
# Licence:     <your licence>
#-------------------------------------------------------------------------------

import pygame as pyg
import os

class Pantalla:
    def __init__(self):
        os.environ['SDL_VIDEO_CENTERED'] = '0'
        self.COLORFONDO=pyg.Color(20,20,70)
        self.COLORDIBUJO=pyg.Color(40,40,40)
        self.MEDIDA=self.ANCHO,self.ALTO=800,600
        self.FUENTE=pyg.font.SysFont("Brush Script MT",38)
        self.SONG_END = pyg.USEREVENT + 1
        self.FPS = 15
        self.FONDO=pyg.image.load('Sprites/Cesped.gif')
        self.CLOCK=pyg.time.Clock()
        self.FABRICA=FlyweightPersonaje()
        self.TIPOS=[tip.name for tip in TiposPersonajes]
        self.ORDA = []
        self.player = None
        self.TITULO = "(Perdiste)ElJuego.exe"

def main():
    pass

if __name__ == '__main__':
    main()

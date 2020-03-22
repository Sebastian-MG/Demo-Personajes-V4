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

from Flyweight import *
from Tipos import *
import pygame as pyg
import os

class Pantalla:
    def __init__(self, SELECT_PLAYER: str):
        #inicializamos los atributos de la ventana y la centramos
        os.environ['SDL_VIDEO_CENTERED'] = '0'
        self.COLORFONDO=pyg.Color(20,70,20)
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
        self.SELECT_PLAYER = SELECT_PLAYER
        self.MEMENTO = self.player

    def posY(self, npc):
        return npc.getYPos()

    def dibujarInventario(self, marco):
        colorEsp = (0,125,125)
        draw.rect(marco,(0,0,0), (0, 545, 800, 54))
        draw.rect(marco, colorEsp, (55, 546, 53, 53))
        draw.rect(marco, colorEsp, (109, 546, 53, 53))
        try:
            marco.blit(pyg.image.load(self.player.getEquipo("RH").getSprites() + "I.gif"), (55,546))
        except: pass
        try:
            marco.blit(pyg.image.load(self.player.getEquipo("LH").getSprites() + "I.gif"), (109,546))
        except: pass
        for esp in range(self.player.getLenEquipamento()):
            draw.rect(marco,colorEsp, ((esp*54) + 263, 546, 53, 53))
            try:
                marco.blit(pyg.image.load(self.player.getEquipo(esp).getSprites() + "I.gif"), ((esp*54) + 263, 546))
            except: pass

    def iniciarJugador(self):
        self.player = self.FABRICA.addNPC(self.SELECT_PLAYER, [self.ANCHO//2,self.ALTO//2])
        self.player.addEquipo("LH", ObjectFactory.getArmaMadera())
        self.player.addEquipo("RH", ObjectFactory.getEscudoMadera())

    def crearOrda(self):
        for i in range(random.randint(60,80)):
            self.ORDA.append(
                self.FABRICA.addNPC(
                    str(self.TIPOS[random.randint(0,len(self.TIPOS)-1)]),
                    [random.randint(10,self.ANCHO-48),random.randint(10,self.ALTO-64)]))

            while self.ORDA[-1].choque(self.player):
                #aqui se deberia implementar un metodo para teletransportar al npc
                self.ORDA[-1].rect.left = random.randint(5,self.ANCHO-50)
                self.ORDA[-1].setXPos(self.ORDA[-1].rect.left)
                self.ORDA[-1].rect.top = random.randint(5,self.ALTO-50)
                self.ORDA[-1].setYPos(self.ORDA[-1].rect.top)

            for npc in range(len(self.ORDA)-1):
                #aqui se podria implementar un observador
                if npc<0:
                    break
                if self.ORDA[npc].choque(self.ORDA[-1]) or self.ORDA[-1].getXPos()<=5 or self.ORDA[-1].getYPos()<=5 or self.ORDA[-1].getXPos()>=self.ANCHO-43 or self.ORDA[-1].getYPos()>=self.ALTO-111 or self.ORDA[npc].getVida()<=0:
                    self.ORDA.pop(-1)
                    break

            #esto se remplazara en los prototype
            if random.randint(0,2)==0: self.ORDA[-1].addEquipo("RH", ObjectFactory.getArmaMadera())
            if random.randint(0,2)==0: self.ORDA[-1].addEquipo("LH", ObjectFactory.getEscudoMadera())

            self.ORDA[-1].update()


def main():
    pyg.init()
    pantalla = Pantalla("Pruebas")
    pass

if __name__ == '__main__':
    main()

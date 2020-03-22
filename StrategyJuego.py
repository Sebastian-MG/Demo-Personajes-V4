#-------------------------------------------------------------------------------
# Name:        module1
# Purpose:
#
# Author:      estudiantes
#
# Created:     24/02/2020
# Copyright:   (c) estudiantes 2020
# Licence:     <your licence>
#-------------------------------------------------------------------------------

from State import *
import pygame as pyg
import random

class StrategyJuego:
    def __init__(self):
        self._juego = None
        self._pantalla = None
        self._ventana = None

    def setJuego(self, juego):
        self._juego = juego

    def setPantalla(self, win):
        self._pantalla = win

    def setVentana(self, marco):
        self._ventana = marco

    def getJuego(self):
        return self._juego

    def getPantalla(self):
        return self._pantalla

    def getVentana(self):
        return self._ventana

    def execute(self):
        pass

class StrategyJugar(StrategyJuego):
    def execute(self):
        for event in pyg.event.get():
            if event.type == pyg.QUIT:
                pyg.quit()
                quit()
            if event.type == pyg.KEYUP:
                if event.key==pyg.K_ESCAPE:
                    pyg.quit()
                    quit()
                if event.key == pyg.K_LEFT:
                    self._pantalla.player.setXVel(0)
                    self._pantalla.player.ind = 0
                if event.key == pyg.K_RIGHT:
                    self._pantalla.player.setXVel(0)
                    self._pantalla.player.ind = 0
                if event.key == pyg.K_UP:
                    self._pantalla.player.setYVel(0)
                    self._pantalla.player.ind = 0
                if event.key == pyg.K_DOWN:
                    self._pantalla.player.setYVel(0)
                    self._pantalla.player.ind = 0
                if event.key == pyg.K_x or event.key == pyg.K_z or event.key == pyg.K_c:
                    self._pantalla.player.getStado().__init__(self._pantalla.player)
                if event.key == pyg.K_SPACE:
                    print("Entro")
                    self._juego = StrategyPausa()
                    self._juego.setJuego(self._juego)
                    self._juego.setPantalla(self._pantalla)
                    self._juego.setVentana(self._ventana)
            if event.type == pyg.KEYDOWN:
                if event.key == pyg.K_LEFT:
                    self._pantalla.player.setXVel(-5)
                    self._pantalla.player.setStado(StatePersL(self._pantalla.player))
                if event.key == pyg.K_RIGHT:
                    self._pantalla.player.setXVel(5)
                    self._pantalla.player.setStado(StatePersR(self._pantalla.player))
                if event.key == pyg.K_UP:
                    self._pantalla.player.setYVel(-5)
                    self._pantalla.player.setStado(StatePersU(self._pantalla.player))
                if event.key == pyg.K_DOWN:
                    self._pantalla.player.setYVel(5)
                    self._pantalla.player.setStado(StatePersD(self._pantalla.player))
                if event.key == pyg.K_p:
                    t = self._pantalla.player
                    self._pantalla.MEMENTO.adapter(self._pantalla.MEMENTO, self._pantalla.player)
                    self._pantalla.player = self._pantalla.MEMENTO
                    self._pantalla.MEMENTO = t
                if event.key == pyg.K_q:
                    #esto sera editado despues para que un menu aparezca con
                    #las opciones de equipamiento
                    t = self._pantalla.player.getEquipo("0")
                    self._pantalla.player.modEquipo("0", self._pantalla.player.getEquipo("RH"))
                    self._pantalla.player.modEquipo("RH", t)
                if event.key == pyg.K_w:
                    #esto sera editado despues para que un menu aparezca con
                    #las opciones de equipamiento
                    t = self._pantalla.player.getEquipo("1")
                    self._pantalla.player.modEquipo("1", self._pantalla.player.getEquipo("LH"))
                    self._pantalla.player.modEquipo("LH", t)
                if event.key == pyg.K_x:
                    self._pantalla.player.images = [self._pantalla.player.getSprites()[self._pantalla.player.getStado().getDir()]["Atk"][i] for i in [1,2,1]]
                if event.key == pyg.K_z:
                    self._pantalla.player.images = [self._pantalla.player.getSprites()[self._pantalla.player.getStado().getDir()]["Dir"][i] for i in range(3)]
                    self._pantalla.player.images[0] = self._pantalla.player.getSprites()[self._pantalla.player.getStado().getDir()]["Atk"][0]
                if event.key == pyg.K_c:
                    self._pantalla.player.images = [self._pantalla.player.getSprites()[self._pantalla.player.getStado().getDir()]["Def"][0] for i in range(3)]
                if event.key == pyg.K_a:
                    self._pantalla.ORDA.append(
                        self._pantalla.FABRICA.addNPC(
                            str(self._pantalla.TIPOS[random.randint(0,len(self._pantalla.TIPOS)-1)]),
                            [random.randint(10,self._pantalla.ANCHO-48),random.randint(10,self._pantalla.ALTO-64)]))

        print("Jugando")
        self._pantalla.player.update()
        self._ventana.fill(self._pantalla.COLORFONDO)
        self._pantalla.dibujarInventario(self._ventana)
        #VENTANA.blit(FONDO, pyg.Rect(0, 0, ANCHO, ALTO))
        for npc in self._pantalla.ORDA:
            npc.existir(random.randint(0,8), random.randint(0,9))
            if self._pantalla.player.choque(npc):
                self._pantalla.player.modVida(-1*npc.getFuerza())
                npc.modVida(-1*self._pantalla.player.getFuerza())
            else:
                for anotNpc in self._pantalla.ORDA:
                    if anotNpc==npc:
                        continue
                    if npc.choque(self._pantalla.player):
                        npc.existir(0,0)
                    if npc.choque(anotNpc):
                        npc.existir(None,10)
                        anotNpc.modVida(-1*npc.getFuerza())
            if npc.getXPos()<=5 or npc.getYPos()<=5 or npc.getXPos()>=self._pantalla.ANCHO-43 or npc.getYPos()>=self._pantalla.ALTO-111 or npc.getVida()<=0:
                self._pantalla.ORDA.remove(npc)
                break
            npc.update()

        self._pantalla.ORDA.append(self._pantalla.player)
        self._pantalla.ORDA.sort(key=self._pantalla.posY)

        '''if player is JUGABILIDAD.player:
            print(True)'''
        for npc in self._pantalla.ORDA:
            npc.draw(self._ventana)

        self._pantalla.ORDA.remove(self._pantalla.player)

        #print(player, player.getEquipo("RH").getDurabilidad())

        pyg.display.update()
        #print(gc.get_threshold())
        self._pantalla.CLOCK.tick(self._pantalla.FPS)

class StrategyPausa(StrategyJuego):
    def execute(self):
        for event in pyg.event.get():
            if event.type == pyg.QUIT:
                pyg.quit()
                quit()
            if event.type == pyg.KEYUP:
                if event.key==pyg.K_ESCAPE:
                    pyg.quit()
                    quit()
                if event.key == pyg.K_SPACE:
                    print("Entro")
                    self._juego = StrategyJugar()
                    self._juego.setJuego(self._juego)
                    self._juego.setPantalla(self._pantalla)
                    self._juego.setVentana(self._ventana)
        print("Pausado")
        pyg.display.update()
        #print(gc.get_threshold())
        pyg.time.Clock().tick(60)

def main():
    for event in pyg.event.get():
        if event.type == pyg.QUIT:
            pyg.quit()
            quit()
        if event.type == pyg.KEYUP:
            if event.key==pyg.K_ESCAPE:
                pyg.quit()
                quit()
            if event.key == pyg.K_LEFT:
                player.setXVel(0)
                player.ind = 0
            if event.key == pyg.K_RIGHT:
                player.setXVel(0)
                player.ind = 0
            if event.key == pyg.K_UP:
                player.setYVel(0)
                player.ind = 0
            if event.key == pyg.K_DOWN:
                player.setYVel(0)
                player.ind = 0
            if event.key == pyg.K_x or event.key == pyg.K_z or event.key == pyg.K_c:
                player.getStado().__init__(player)
        if event.type == pyg.KEYDOWN:
            if event.key == pyg.K_LEFT:
                player.setXVel(-5)
                player.setStado(StatePersL(player))
            if event.key == pyg.K_RIGHT:
                player.setXVel(5)
                player.setStado(StatePersR(player))
            if event.key == pyg.K_UP:
                player.setYVel(-5)
                player.setStado(StatePersU(player))
            if event.key == pyg.K_DOWN:
                player.setYVel(5)
                player.setStado(StatePersD(player))
            if event.key == pyg.K_p:
                t = player
                saves.adapter(saves, player)
                player = saves
                saves = t
            if event.key == pyg.K_q:
                #esto sera editado despues para que un menu aparezca con
                #las opciones de equipamiento
                t = player.getEquipo("0")
                player.modEquipo("0", player.getEquipo("RH"))
                player.modEquipo("RH", t)
            if event.key == pyg.K_w:
                #esto sera editado despues para que un menu aparezca con
                #las opciones de equipamiento
                t = player.getEquipo("1")
                player.modEquipo("1", player.getEquipo("LH"))
                player.modEquipo("LH", t)
            if event.key == pyg.K_x:
                player.images = [player.getSprites()[player.getStado().getDir()]["Atk"][i] for i in [1,2,1]]
            if event.key == pyg.K_z:
                player.images = [player.getSprites()[player.getStado().getDir()]["Dir"][i] for i in range(3)]
                player.images[0] = player.getSprites()[player.getStado().getDir()]["Atk"][0]
            if event.key == pyg.K_c:
                player.images = [player.getSprites()[player.getStado().getDir()]["Def"][0] for i in range(3)]
            if event.key == pyg.K_a:
                ORDA.append(
                    FABRICA.addNPC(
                    str(TIPOS[random.randint(0,len(TIPOS)-1)]),
                    [random.randint(10,ANCHO-48),random.randint(10,ALTO-64)]))

    player.update()
    VENTANA.fill(COLORFONDO)
    dibujarInventario(VENTANA, player)
    #VENTANA.blit(FONDO, pyg.Rect(0, 0, ANCHO, ALTO))
    for npc in ORDA:
        npc.existir(random.randint(0,8), random.randint(0,9))
        if player.choque(npc):
            player.modVida(-1*npc.getFuerza())
            npc.modVida(-1*player.getFuerza())
        else:
            for anotNpc in ORDA:
                if anotNpc==npc:
                    continue
                if npc.choque(player):
                    npc.existir(0,0)
                if npc.choque(anotNpc):
                    npc.existir(None,10)
                    anotNpc.modVida(-1*npc.getFuerza())
        if npc.getXPos()<=5 or npc.getYPos()<=5 or npc.getXPos()>=ANCHO-43 or npc.getYPos()>=ALTO-111 or npc.getVida()<=0:
            ORDA.remove(npc)
            break
        npc.update()

    ORDA.append(player)
    ORDA.sort(key=posY)

    '''if player is JUGABILIDAD.player:
        print(True)'''
    for npc in ORDA:
        npc.draw(VENTANA)

    ORDA.remove(player)

    #print(player, player.getEquipo("RH").getDurabilidad())

    pyg.display.update()
    #print(gc.get_threshold())
    CLOCK.tick(FPS)
    pass

if __name__ == '__main__':
    main()

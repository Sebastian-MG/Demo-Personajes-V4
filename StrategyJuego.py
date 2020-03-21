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

import pygame as pyg

class StrategyJuego:
    def __init__(self):
        self._juego = None

    def setJuego(self, juego):
        self._juego = juego

    def getJuego(self):
        return self._juego

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
                if event.key == pyg.K_SPACE:
                    print("Entro")
                    self._juego = StrategyPausa()
                    self._juego.setJuego(self._juego)
        print("Jugando")
        pyg.display.update()
        #print(gc.get_threshold())
        pyg.time.Clock().tick(60)

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
                    self._juego = StrategyPausa()
                    self._juego.setJuego(self._juego)
        print("Pausado")
        pyg.display.update()
        #print(gc.get_threshold())
        pyg.time.Clock().tick(60)
def main():
    pass

if __name__ == '__main__':
    main()

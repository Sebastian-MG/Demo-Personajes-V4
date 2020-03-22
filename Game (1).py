#-------------------------------------------------------------------------------
# Name:        TheGame
# Purpose:
#
# Author:      alguien
#
# Created:     16/09/2077
# Copyright:   (c) lenovo 2019
# Licence:     <your licence>
#-------------------------------------------------------------------------------

from StrategyJuego import *
from Decorator import *
from Pantalla import *
import os, gc
import pygame as pyg

def main(SELECT_PLAYER: str = "Pruebas"):
    #inicializacion pygame
    pyg.init()

    #creamos la pantalla
    pantalla = Pantalla(SELECT_PLAYER)

    #inicializar la ventana
    VENTANA=pyg.display.set_mode(pantalla.MEDIDA)
    pyg.display.set_caption(pantalla.TITULO)

    #hacer invisible el mouse
    #pyg.mouse.set_visible(False)

    #inicializar sonido de fondo
    pyg.mixer.music.set_endevent(pantalla.SONG_END)
    #pyg.mixer.music.load('Efects/Flash.mp3')
    #pyg.mixer.music.play()

    #inicializando al personaje principal (jugable)
    pantalla.iniciarJugador()

    #asignandole un decorador en el memento de nuestro personaje
    pantalla.MEMENTO = DcPersonajeLadron(pantalla.player)

    #inicializando poblacion
    pantalla.crearOrda()

    JUGABILIDAD = StrategyJugar()
    JUGABILIDAD.setJuego(JUGABILIDAD)
    JUGABILIDAD.setPantalla(pantalla)
    JUGABILIDAD.setVentana(VENTANA)

    while pantalla.player.getVida() > 0:
        JUGABILIDAD.execute()
        JUGABILIDAD = JUGABILIDAD.getJuego()

    pyg.quit()
    print("Felicidades, Perdiste EL JUEGO")
    pass

if __name__ == '__main__':
    main()

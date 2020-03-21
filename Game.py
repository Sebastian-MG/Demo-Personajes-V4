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

from Flyweight import *
from Decorator import *
from Tipos import *
from StrategyJuego import *
import os, gc
import pygame as pyg
import random


def posY(npc):
    return npc.getYPos()

def dibujarInventario(marco, player):
    colorEsp = (0,125,125)
    draw.rect(marco,(0,0,0), (0, 545, 800, 54))
    draw.rect(marco,colorEsp, (55, 546, 53, 53))
    draw.rect(marco,colorEsp, (109, 546, 53, 53))
    try:
        marco.blit(pyg.image.load(player.getEquipo("RH").getSprites() + "I.gif"), (55,546))
    except: pass
    try:
        marco.blit(pyg.image.load(player.getEquipo("LH").getSprites() + "I.gif"), (109,546))
    except: pass
    for esp in range(player.getLenEquipamento()):
        draw.rect(marco,colorEsp, ((esp*54) + 263, 546, 53, 53))
        try:
            marco.blit(pyg.image.load(player.getEquipo(esp).getSprites() + "I.gif"), ((esp*54) + 263, 546))
        except: pass

def main(SELECT_PLAYER: str = "Pruebas"):
    #inicializacion pygame
    pyg.init()

    '''inicializamos todo tipo
    de constantes y centrar la ventana'''
    os.environ['SDL_VIDEO_CENTERED'] = '0'
    COLORFONDO=pyg.Color(20,20,70)
    COLORDIBUJO=pyg.Color(40,40,40)
    MEDIDA=ANCHO,ALTO=800,600
    FUENTE=pyg.font.SysFont("Brush Script MT",38)
    SONG_END = pyg.USEREVENT + 1
    FPS = 15
    FONDO=pyg.image.load('Sprites/Cesped.gif')
    CLOCK=pyg.time.Clock()
    FABRICA=FlyweightPersonaje()
    TIPOS=[tip.name for tip in TiposPersonajes]
    ORDA = []
    player = None
    TITULO = "(Perdiste)ElJuego.exe"

    #inicializar la ventana
    VENTANA=pyg.display.set_mode(MEDIDA)
    pyg.display.set_caption(TITULO)

    #hacer invisible el mouse
    #pyg.mouse.set_visible(False)

    #inicializar sonido de fondo
    pyg.mixer.music.set_endevent(SONG_END)
    #pyg.mixer.music.load('Efects/Flash.mp3')
    #pyg.mixer.music.play()

    #inicializando al personaje principal (jugable)
    player = FABRICA.addNPC(SELECT_PLAYER, [ANCHO//2,ALTO//2])
    player.addEquipo("LH", ObjectFactory.getArmaMadera())
    player.addEquipo("RH", ObjectFactory.getEscudoMadera())
    saves=player
    player = DcPersonajeLadron(player)
    player = DcPersonajeLadronLH(player)

    #inicializando poblacion
    #for i in range(random.randint(5,10)):
    for i in range(random.randint(60,80)):
        ORDA.append(
            FABRICA.addNPC(
                str(TIPOS[random.randint(0,len(TIPOS)-1)]),
                [random.randint(10,ANCHO-48),random.randint(10,ALTO-64)]))
        while ORDA[-1].choque(player):
            ORDA[-1].rect.left = random.randint(5,ANCHO-50)
            ORDA[-1].setXPos(ORDA[-1].rect.left)
            ORDA[-1].rect.top = random.randint(5,ALTO-50)
            ORDA[-1].setYPos(ORDA[-1].rect.top)
        for npc in range(len(ORDA)-1):
            if npc<0:
                break
            if ORDA[npc].choque(ORDA[-1]) or ORDA[-1].getXPos()<=5 or ORDA[-1].getYPos()<=5 or ORDA[-1].getXPos()>=ANCHO-43 or ORDA[-1].getYPos()>=ALTO-111 or ORDA[npc].getVida()<=0:
                ORDA.pop(-1)
                break
        ORDA[-1].setFuerza(random.randint(3,5))
        if random.randint(0,2)==0: ORDA[-1].addEquipo("RH", ObjectFactory.getArmaMadera())
        if random.randint(0,2)==0: ORDA[-1].addEquipo("LH", ObjectFactory.getEscudoMadera())
        ORDA[-1].update()
    #print(npc.getSprites()["D"][0][-1].upper())

    JUGABILIDAD = StrategyJugar()
    JUGABILIDAD.setJuego(JUGABILIDAD)

    '''while True:
        JUGABILIDAD.execute()
        JUGABILIDAD = JUGABILIDAD.getJuego()
        print("En curso",JUGABILIDAD)
        print("En clase",JUGABILIDAD.getJuego())
    '''
    while player.getVida() > 0:
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
    pyg.quit()
    print("Felicidades, Perdiste EL JUEGO")
    pass

if __name__ == '__main__':
    main()

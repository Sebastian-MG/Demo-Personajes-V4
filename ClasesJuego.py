#-------------------------------------------------------------------------------
# Name:        ClasesJuego
# Purpose:     Ninguno, una nota
#
# Author:      Pedro Barr, Felipe, Sebastian Mancera
#
# Created:     19/09/1999
# Copyright:   (c) lenovo 2019
# Licence:     <your licence>
#-------------------------------------------------------------------------------

from State import *
from pygame import sprite, image, draw
import random

#Clase padre equipamento (Dispuesta a cambios, y a ser extendible)
class Equipamento(sprite.Sprite):

    '''El atributo efecto podria ser confus
    en la ejecucion, posiblemente lo reemplazemos'''
    _material=None
    _sprites = None
    _efecto = None
    _durabilidad = None

    def __init__(self):
        sprite.Sprite.__init__(self)

    #getters (obviamente)
    def getMaterial(self) -> str:
        return self._material

    def getSprites(self) -> dict:
        return self._sprites

    def getEfecto(self):
        return self._efecto

    def getDurabilidad(self) -> int:
        return self._durabilidad

    #setters (obviamente)
    def setMaterial(self, mat: str):
        self._material = mat

    def setSprites(self, sprts: dict):
        self._sprites = sprts

    def setEfecto(self, efect):
        self._efecto = efect

    def setDurabilidad(self, dureza: int):
        self._durabilidad = dureza

#Clase hijo Escudo (Dispuesta a cambios)
class Escudo(Equipamento):

    #constructor con el unico atributo propio
    def __init__(self):
        sprite.Sprite.__init__(self)
        ''' el radio se supone que se usara en
        la implementacion'''
        self._radio = None

    #getters (obviamente)
    def getRadio(self):
        return self._radio

    #setters (obviamente)
    def setRadio(self, rad):
        self._radio = rad

    def update(self, direc: str, hand: list):
        self.image = image.load(self.getSprites() + direc + ".gif")
        self.rect=self.image.get_rect()
        self.rect.center = (hand[0], hand[1])
        #self.rect.left = hand[0]
        #self.rect.top =  hand[1]

    #metodo para dibujarse en una ventana
    def draw(self, marco):
        marco.blit(self.image, self.rect)

#Clase hijo Arma (Dispuesta a cambios, y a ser extendible)
class Arma(Equipamento):

    #constructor con el unico atributo propio
    def __init__(self):
        sprite.Sprite.__init__(self)
        #Atributo propio de la clase hijo
        self._factorAtaque = None

    #getters (obviamente)
    def getFactAtaque(self):
        return self._factorAtaque

    #setters (obviamente)
    def setFactAtaque(self, atk):
        self._factorAtaque = atk

    def update(self, direc: str, hand: list):
        self.image = image.load(self.getSprites() + direc + ".gif")
        self.rect=self.image.get_rect()
        self.rect.center = (hand[0], hand[1])

    #metodo para dibujarse en una ventana
    def draw(self, marco):
        marco.blit(self.image, self.rect)

#Clase principal Personaje (Dispuesta a cambios)
class Personaje(sprite.Sprite):

    #constructor con los atributos propios
    def __init__(self):
        sprite.Sprite.__init__(self)
        '''posible implementacion de _velocidad, _direccion, _objetivo'''
        self._tipo=None
        self._equipamento={}
        self._sprites = None
        self._ruido = None
        self._decorados = {}
        self._posicion=None
        self._velocidadX = 0
        self._velocidadY = 0
        self._direccion = 0
        self.ind = 0
        self._vida = 0
        self._maxVida = 0
        self._fuerza = 0
        self._stado = None
        self._velocidadPaso = 0
        self._inercia = 0

    def adapter(self, copia, copiado):
        copia._tipo = copiado.getTipo()
        copia._equipamento = copiado.getEquipamento()
        copia._sprites = copiado.getSprites()
        copia._ruido = copiado.getRuidos()
        copia._decorados = copiado.getDecorados()
        copia._posicion = copiado.getPosicion()
        copia._velocidadX = copiado.getXVel()
        copia._velocidadY = copiado.getYVel()
        copia._direccion = copiado.getDireccion()
        copia.ind = copiado.ind
        copia._vida = copiado.getVida()
        copia._maxVida = copiado.getMaxVida()
        copia._fuerza = copiado.getFuerza()
        copia.rect = copiado.rect
        copia.image = copiado.image
        copia.images = copiado.images
        copia._stado = copiado.getStado()
        copia._stado.__init__(copia)
        copia._velocidadPaso = copiado.getVelocidadPaso()
        copia._inercia = copiado.getInercia()

    #getters (obviamente)
    def getTipo(self) -> str:
        return self._tipo

    def getSprites(self) -> list:
        return self._sprites

    def getRuidos(self) -> list:
        return self._ruido

    def getDecorados(self) -> list:
        return self._decorados

    def getEquipamento(self) -> list:
        return self._equipamento

    def getPosicion(self) -> list:
        return self._posicion

    def getXVel(self) -> int:
        return self._velocidadX

    def getYVel(self) -> int:
        return self._velocidadY

    def getDireccion(self) -> int:
        return self._direccion

    def getVida(self) -> int:
        return self._vida

    def getMaxVida(self) -> int:
        return self._maxVida

    def getFuerza(self) -> int:
        return self._fuerza

    def getStado(self):
        return self._stado

    def getVelocidadPaso(self):
        return self._velocidadPaso

    def getInercia(self):
        return self._inercia

    #setters (obviamente)
    def setTipo(self, tip: str):
        self._tipo = tip

    def setSprites(self, sprts: list):
        self._sprites = sprts

    def setRuido(self, rudo: list):
        self._ruido = rudo

    def setDecorados(self, decor: list):
        self._decorados = decor

    def setEquipamento(self, equipo: list):
        self._equipamento = equipo

    def setPosicion(self, pos: list):
        self._posicion = pos

    def setXVel(self, x: int):
        self._velocidadX = x

    def setYVel(self, y: int):
        self._velocidadY = y

    def setDireccion(self, direct: int):
        self._direccion = direct

    def setVida(self, vita: int):
        self._vida = vita

    def setMaxVida(self, maxVida):
        self._maxVida = maxVida

    def setFuerza(self, mayfourth: int):
        self._fuerza = mayfourth

    def setStado(self, state):
        self._stado = state

    def setVelocidadPaso(self, velP):
        self._velocidadPaso = velP

    def setInercia(self, I):
        self._inercia = I

    #metodos propios de la clase

    #vacia el inventario de objetos
    def clearEquipamento(self) -> None:
        self.setEquipamento({})

    #Añade o remplaza un objeto en el inventario
    def addEquipo(self, key, equipo):
        self._equipamento[str(key)] = equipo

    #modifica un objeto en el inventario, llamando al metodo addEquipo
    def modEquipo(self, key, equipo):
        '''
        Metodo para modificar o crear un espacio de equipo en
        el inventario del personaje

        Arguments:
            key (str): La direccion en el inventario a modificar
            equipo (Equipamento): El objeto equipamento que se introducira
        '''
        self.addEquipo(key, equipo)

    #elimina un objeto del inventario
    def popEquipo(self, key):
        self._equipamento.pop(str(key))

    #getter de la cantidad de objetos en el inventario (sin manos)
    def getLenEquipamento(self) -> int:
        n=0
        if "RH" in self._equipamento:
            n+=1
        if "LH" in self._equipamento:
            n+=1
        return len(self._equipamento)-n

    #getter para un objeto en el inventario
    def getEquipo(self, key: str) -> Equipamento:
        return self._equipamento[str(key)]

    #getters de la posicion en X y Y
    def getXPos(self) -> int:
        return self._posicion[0]

    def getYPos(self) -> int:
        return self._posicion[1]

    #setters de la posicion X y Y:
    def setXPos(self, x: int):
        self._posicion[0] = x

    def setYPos(self, y: int):
        self._posicion[1] = y

    #añade un decorador
    def addDecor(self, clave: str, decor: sprite):
        self._decorados[str(clave)] = decor

    #elimina un decorador
    def popDecor(self, clave: str):
        self._decorados.pop(str(clave))

    #devuelve la cantidad de decoradores
    def getLenDecor(self) -> int:
        n=0
        if "Smbr" in self._decorados:
            n+=1
        return len(self._decorados)-n

    #Modificador de vida
    def modVida(self, modif: int):
        self.setVida(self.getVida() + modif)
        if self.getVida() > self.getMaxVida():
            self.setVida(self.getMaxVida())
        elif self.getVida() <= 0:
            self.setVida(0)

    #Metodo que define si se ha chocado con algun objeto
    def choque(self, obj) -> bool:
        if self.rect.colliderect(obj.rect):
            return True
        return False

    #Metodo que invierte la direccion en la que va el personaje
    def invertDir(self, direct: int) -> int:
        if direct == 0:
            return random.randint(1,8)
        if direct <= 4:
            n=4
        elif direct <= 8:
            n=-4
        return direct + n

    #Metodo que hace a los NPCs moverse solos por el ambiente
    def existir(self, direct: int, factor_cambio: int, objetivo=None):
        '''
        direct (int)
        '''
        if factor_cambio == 10:
            direct = self.invertDir(self._direccion)
        elif factor_cambio <= 5:
            direct = 0
        elif factor_cambio <= 8:
            direct = self._direccion
        else:
            direct = direct
        if direct==0:
            self.setXVel(0)
            self.setYVel(0)
            self.ind = 0
        elif direct==1:
            self.setXVel(-5)
            self.setYVel(-5)
            self.setStado(StatePersU(self))
        elif direct==2:
            self.setXVel(0)
            self.setYVel(-5)
            self.setStado(StatePersU(self))
        elif direct==3:
            self.setXVel(5)
            self.setYVel(-5)
            self.setStado(StatePersR(self))
        elif direct==4:
            self.setXVel(5)
            self.setYVel(0)
            self.setStado(StatePersR(self))
        elif direct==5:
            self.setXVel(5)
            self.setYVel(5)
            self.setStado(StatePersD(self))
        elif direct==6:
            self.setXVel(0)
            self.setYVel(5)
            self.setStado(StatePersD(self))
        elif direct==7:
            self.setXVel(-5)
            self.setYVel(5)
            self.setStado(StatePersL(self))
        elif direct==8:
            self.setXVel(-5)
            self.setYVel(0)
            self.setStado(StatePersL(self))
        self._direccion = direct

    #Metodos para hallar el centro de la mano izquierda y derecha
    def centroLH(self) -> list:
        return self._stado.getLHand()

    def centroRH(self) -> list:
        return self._stado.getRHand()

    def update(self):
        if self.getXVel()==0 and self.getYVel()==0:
            self.image = image.load(self.images[0])
            self.ind=0
        else:
            self.ind +=1
            aux_vel = self._velocidadPaso
            if self.ind <= self._velocidadPaso:
                self.image = image.load(self.images[1])
            elif self.ind <= 2*self._velocidadPaso:
                self.image = image.load(self.images[2])
                if self.ind == 2*self._velocidadPaso:
                    self.ind = 0
        self.rect=self.image.get_rect()
        self.rect.left = self.getXPos() + self.getXVel()
        self.setXPos(self.rect.left)
        self.rect.top = self.getYPos() + self.getYVel()
        self.setYPos(self.rect.top)
        aux_dir = self._stado.getDir()
        centro = self.centroLH()
        if 'LH' in self.getEquipamento().keys() and self.getEquipo('LH'):
            self.getEquipo("LH").update(aux_dir,[self.getXPos() + centro[0], self.getYPos() + centro[1]])
        centro = self.centroRH()
        if 'RH' in self.getEquipamento().keys() and self.getEquipo('RH'):
            self.getEquipo("RH").update(aux_dir,[self.getXPos() + centro[0], self.getYPos() + centro[1]])

    def drawSombra(self, marco):
        marco.blit(image.load(self.getDecorados()["Smbr"]), (self.getXPos() + 5 ,self.getYPos() + 42))

    def drawBarraVida(self, marco):
        draw.rect(marco,(
            255-abs(int(255*((self._vida/self._maxVida)**8))),
            abs(int(255*((self._vida/self._maxVida)**2))),
            0),
            (self.getXPos(), self.getYPos() - 7, 37*(self._vida/self._maxVida), 5))

    #metodo para dibujarse en una ventana
    def draw(self, marco):
        self.drawSombra(marco)
        self.drawBarraVida(marco)
        self._stado.draw(marco)

#pruebas del manejo de las clases
def main():
    #blablabla, creamos un personaje vacio de nombre generico
    pers = Personaje()
    pers.setTipo("Link")
    pers.setSprites(["",""])
    pers.setRuido([""])
    pers.setPosicion([0,0])

    '''Añadimos un arma y un escudo generico a su

    mano derecha (RH) y su mano izquierda (LH)'''
    pers.addEquipo("RH", Arma())
    pers.addEquipo("LH", Escudo())

    '''Añadimos un objetos genericos en posiciones
    genericas de su inventario'''
    for i in range(3):
        pers.addEquipo(pers.getLenEquipamento()+1,Equipamento())

    '''Llenamos genericamente los atributos de
    los objetos en su inventario'''
    for keys in pers.getEquipamento():
        pers.getEquipo(keys).setMaterial("Madera")
        pers.getEquipo(keys).setDurabilidad(50)
        if keys=="LH":
            pers.getEquipo(keys).setRadio(1)
        elif keys=="RH":
            pers.getEquipo(keys).setFactAtaque(5)

    '''eliminamos el elemento en posicion 3
    del inventario (para probar el metodo pop)'''
    pers.popEquipo(3)

    '''eliminamos todo en el inventario
    (para probar los metodos get, set y clear )'''
    dicc=pers.getEquipamento()
    pers.clearEquipamento()
    pers.setEquipamento(dicc)

    '''remplazamos el escudo generico por uno más
    especifico (para probar el metodo mod)'''
    sqdo=Escudo()
    sqdo.setMaterial("Metal")
    sqdo.setDurabilidad(70)
    sqdo.setEfecto(None)
    sqdo.setRadio(5)
    pers.modEquipo("LH",sqdo)

    '''imprimimos todo para validar que todos
    los cambios han sido correctos (easy peasy)'''
    print(pers.getTipo(),":",pers.getSprites(),",",pers.getRuidos())
    for keys in pers.getEquipamento():
        print(keys,"->",pers.getEquipo(keys).getMaterial(), pers.getEquipo(keys).getDurabilidad(), end=" ")
        if keys=="LH":
            print(pers.getEquipo(keys).getRadio())
        elif keys=="RH":
            print(pers.getEquipo(keys).getFactAtaque())
        else:
            print()
    pass

if __name__ == '__main__':
    main()


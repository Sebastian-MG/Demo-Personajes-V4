#-------------------------------------------------------------------------------
# Name:        Decorator
# Purpose:     Ninguno, una nota
#
# Author:      Pedro Barr, Felipe, Sebastian Mancera
#
# Created:     19/09/1999
# Copyright:   (c) lenovo 2019
# Licence:     <your licence>
#-------------------------------------------------------------------------------

'''importe de Clases Bases'''
from ClasesJuego import *

'''Notacion: Dc + (Objeto a decorar +) Nombre del decorador
que hereda la clase del objeto a decorar, para poder usarlo
como un objeto de esa clase en la ejecucion'''

#Decorador de Personaje, que afecta el radio de Choque
class DcPersonaje(Personaje):

    #construye el objeto igual al que le es dado
    def __init__(self, personaje: Personaje):
        sprite.Sprite.__init__(self)
        self._persDecorado = personaje
        self.adapter(self, self._persDecorado)

    def getDecorado(self):
        return self._persDecorado

class DcPersonajeLadron(DcPersonaje):

    #decorador que define si se ha chocado con algun objeto
    def choque(self, obj: Personaje) -> bool:
        self._persDecorado.rect = self.rect
        self._persDecorado.choque(obj)
        rect = self.rect#.inflate(50, 50)
        if rect.colliderect(obj.rect):
            obj.modEquipo("RH", None)
            return True
        return False

class DcPersonajeLadronLH(DcPersonaje):

    #decorador que define si se ha chocado con algun objeto
    def choque(self, obj: Personaje) -> bool:
        self._persDecorado.rect = self.rect
        self._persDecorado.choque(obj)
        rect = self.rect#.inflate(50, 50)
        if rect.colliderect(obj.rect):
            obj.modEquipo("LH", None)
            return True
        return False

class DcPersonajeCrabs(DcPersonaje):

    #decorador que define si se ha chocado con algun objeto
    def update(self):
        print(self.getEquipo("RH").getSprites())
        if self.getXVel()==0 and self.getYVel()==0:
            self.image = image.load(self.images[0])
            aux_ind=0
        else:
            self.ind +=1
            aux_vel = 3
            if self.ind <= aux_vel:
                self.image = image.load(self.images[1])
                aux_ind=1
            elif self.ind <= 2*aux_vel:
                self.image = image.load(self.images[2])
                aux_ind=2
            else:
                self.image = image.load(self.images[2])
                aux_ind=2
                self.ind = 0
        self.rect=self.image.get_rect()
        self.rect.left = self.getXPos() + self.getXVel()
        self.setXPos(self.rect.left)
        self.rect.top = self.getYPos() + self.getYVel()
        self.setYPos(self.rect.top)
        if self.getSprites()["U"] is self.images:
            aux_dir="U"
        if self.getSprites()["D"] is self.images:
            aux_dir="D"
        if self.getSprites()["L"] is self.images:
            aux_dir="L"
        if self.getSprites()["R"] is self.images:
            aux_dir="R"
        centro = self.centroLH(aux_dir,aux_ind)
        if 'LH' in self.getEquipamento().keys() and self.getEquipo('LH'):
            self.getEquipo("LH").update(aux_dir,[self.getXPos() + centro[0], self.getYPos() + centro[1]])
        centro = self.centroRH(aux_dir,aux_ind)
        if 'RH' in self.getEquipamento().keys() and self.getEquipo('RH'):
            self.getEquipo("RH").update(aux_dir,[self.getXPos() + centro[0], self.getYPos() + centro[1]])

#Decorador de Arma, que afecta el efecto que devuelve el arma
class DcArmaDobleFilo(Arma):

    #construye el objeto igual al que le es dado
    def __init__(self, arma: Arma):
        sprite.Sprite.__init__(self)
        self._material = arma.getMaterial()
        self._sprites = arma.getSprites()
        self._efecto = arma.getEfecto()
        self._durabilidad = arma.getDurabilidad()
        self._factorAtaque = arma.getFactAtaque()

    #decorador para que al devolver el efecto sea uno nuevo
    def getEfecto(self) -> str:
        return "Menos uno al portador o lo que sea"

#Decorador de Arma, que afecta el factor de ataque que devuelve el arma
class DcArmaPotenciada(Arma):

    #construye el objeto igual al que le es dado
    def __init__(self, arma: Arma):
        sprite.Sprite.__init__(self)
        self._material = arma.getMaterial()
        self._sprites = arma.getSprites()
        self._efecto = arma.getEfecto()
        self._durabilidad = arma.getDurabilidad()
        self._factorAtaque = arma.getFactAtaque()

    #decorador para que al devolver el factor de ataque sea el cuadrado
    def getFactAtaque(self) -> int:
        return self._factorAtaque**2

#pruebas del manejo de las clases
def main():
    #se crea un personaje y se le crea un arma generica en la mano derecha (RH)
    pers = Personaje()
    pers.addEquipo("RH", Arma())
    pers.getEquipo("RH").setMaterial("Madera")
    pers.getEquipo("RH").setDurabilidad(50)
    pers.getEquipo("RH").setFactAtaque(5)

    #se imprime para probar
    print(pers.getEquipo("RH").getFactAtaque())
    print(pers.getEquipo("RH").getEfecto())

    '''se modifica el arma, remplazando por
    un arma decorada'''
    pers.modEquipo("RH",DcArmaDobleFilo(DcArmaPotenciada(pers.getEquipo("RH"))))

    '''se modifica el choque, remplazando por
    un choque decorado'''
    pers = DcPersonajeChoqueAumento(pers)

    #se imprime y se comprueba
    print(pers.getEquipo("RH").getFactAtaque())
    print(pers.getEquipo("RH").getEfecto())
    pass

if __name__ == '__main__':
    main()

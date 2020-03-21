#-------------------------------------------------------------------------------
# Name:        Abstract (Factory)
# Purpose:     Ninguno, una nota
#
# Author:      Pedro Barr, Felipe, Sebastian Mancera
#
# Created:     19/09/1999
# Copyright:   (c) lenovo 2019
# Licence:     <your licence>
#-------------------------------------------------------------------------------

#importar Builder
from Builder import *

#Clase abstracta AbstractFactory
class AbstractFactory:
    #objeto a fabricar
    _builders = None

    #getter (obviamente)
    def getBuiders(self):
        return self._builders

#Fabrica para personajes
class FactoryPersonaje(AbstractFactory):

    #Los productos que ensambla esta fabrica son solo builders
    def __init__(self):
        '''Para un personaje se necesitan
        tres builders, uno para Sprites,
        uno para sonidos, otro (opcional)
        para la sombra y los efectos'''
        self._builders={"Sprt": BuilderSprites(), "Sond": BuildSonidos()}

#Fabrica para objetos de inventario
class FactoryEquipamento(AbstractFactory):

    #Los productos que ensambla esta fabrica son solo builders
    def __init__(self):
        '''Para un equipo se necesitan
        tres builders, uno para Sprites,
        uno para sonidos, otro (opcional)
        para la sombra y los efectos'''
        self._builders={"Sprt": BuilderSprites(), "Sond": BuildSonidos()}

#es inecesario probarla
def main():
    pass

if __name__ == '__main__':
    main()

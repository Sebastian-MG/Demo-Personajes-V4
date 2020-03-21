#-------------------------------------------------------------------------------
# Name:        FlyweightFactory
# Purpose:     Ninguno, una nota
#
# Author:      Pedro Barr, Felipe, Sebastian Mancera
#
# Created:     19/09/1999
# Copyright:   (c) lenovo 2019
# Licence:     <your licence>
#-------------------------------------------------------------------------------

'''importar Prototype'''
from ChainResponsability import *

'''clase FlyweightFactory que genera
personajes en una posicion'''
class FlyweightPersonaje():

    def __init__(self):
        #inicializa la factoria
        ObjectFactory.initialize()

    def addNPC(self, tipo: str, posicion: list) -> Personaje:
        #a traves de un prototipo crea el objeto de peso pluma a usar
        flyweight = Handler().getPersonaje(tipo)

        if flyweight.getTipo()==None:
            '''si no existe un prototipo del
            tipo pedido, genera un personaje y lo inicializa'''
            flyweight.setTipo(tipo)
            fabrica=FactoryPersonaje()
            builders = fabrica.getBuiders()
            builders["Sprt"].setRuta("Personajes/" + flyweight.getTipo())
            builders["Sprt"].MethodDirector()
            builders["Sond"].setRuta("Gritos/" + flyweight.getTipo())
            builders["Sond"].MethodDirector()
            flyweight.setSprites(builders["Sprt"].getBuild())
            flyweight.setRuido(builders["Sond"].getBuild())
            print("No llega a clase", tipo)

        #generar mano derecha e izquierda
        flyweight.addEquipo("RH", None)
        flyweight.addEquipo("LH", None)

        #posiciona al personaje peso de pluma
        flyweight.setPosicion(posicion)
        flyweight.setVelocidadPaso(5)

        #inicializa la imagen
        flyweight.setStado(StatePersD(flyweight))
        flyweight.addDecor("Smbr", "Sprites/Efectos/Smbr.gif")
        flyweight.update()

        return flyweight

#pruebas del manejo de las clases
def main():

    #inicializa la factoria y los prototipos
    factory = FlyweightPersonaje()

    '''creando personajes, totalmente inicializados
    en una posicion, con Sprites, sonidos ( tambien sombras)
    y ya con tipo'''
    pers1 = factory.addNPC("Mago", [0,0])
    pers2 = factory.addNPC("Caballero", [1,1])
    pers3 = factory.addNPC("Prueba", [2,0])
    pers4 = factory.addNPC("Prueba", [0,2])

    #imprime las posiciones para saber que funcionó
    print(pers1.getPosicion(), pers2.getPosicion(), pers3.getPosicion(), pers4.getPosicion())
    pass

if __name__ == '__main__':
    main()

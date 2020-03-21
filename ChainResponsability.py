#-------------------------------------------------------------------------------
# Name:        module1
# Purpose:
#
# Author:      estudiantes
#
# Created:     17/02/2020
# Copyright:   (c) estudiantes 2020
# Licence:     <your licence>
#-------------------------------------------------------------------------------

'''importar Prototype'''
from Prototype import *

class Handler:
    _personaje = None
    _siguiente = None
    _tipo = ""

    def __init__(self):
        self._siguiente = PruebaManejador()

    def getPersonaje(self, tipo: str) -> Personaje:
        if tipo.upper() == self._tipo.upper():
            return self._personaje
        if self._siguiente != None:
            return self._siguiente.getPersonaje(tipo)
        return ObjectFactory.getPersonaje()

class PruebaManejador(Handler):
    def __init__(self):
        self._tipo = "Pruebas"
        self._personaje = ObjectFactory.getPrueba()
        self._siguiente = MagoManejador()

class MagoManejador(Handler):
    def __init__(self):
        self._tipo = "Mago"
        self._personaje = ObjectFactory.getMago()
        self._siguiente = AldeanoManejador()

class AldeanoManejador(Handler):
    def __init__(self):
        self._tipo = "Aldeano"
        self._personaje = ObjectFactory.getAldeano()
        self._siguiente = OrcoManejador()

class OrcoManejador(Handler):
    def __init__(self):
        self._tipo = "Orco"
        self._personaje = ObjectFactory.getOrco()
        self._siguiente = TrollManejador()

class TrollManejador(Handler):
    def __init__(self):
        self._tipo = "Troll"
        self._personaje = ObjectFactory.getTroll()
        self._siguiente = CaballeroManejador()

class CaballeroManejador(Handler):
    def __init__(self):
        self._tipo = "Caballero"
        self._personaje = ObjectFactory.getCaballero()
        self._siguiente = None

def main():
    ObjectFactory.initialize()
    personaje = Handler().getPersonaje("Magodasd")
    print(personaje.getTipo())
    personaje = Handler().getPersonaje("Mago")
    print(personaje.getTipo())
    personaje = Handler().getPersonaje("Prueba")
    print(personaje.getTipo())
    pass

if __name__ == '__main__':
    main()

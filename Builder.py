#-------------------------------------------------------------------------------
# Name:        Builder
# Purpose:     Ninguno, una nota
#
# Author:      Pedro Barr, Felipe, Sebastian Mancera
#
# Created:     19/09/1999
# Copyright:   (c) estudiantes 2019
# Licence:     <your licence>
#-------------------------------------------------------------------------------

#clase abstracta Builder
class Builder:
    #objeto a construir
    _build=None

    #getter (obviamente)
    def getBuild(self):
        return self._build

    #Metodo director
    def MethodDirector(self):
        pass

#Constructor de sprites
class BuilderSprites(Builder):

    def __init__(self):
        #inicializacion para Sprites
        self._build = {"D":{}, "U":{},"L":{}, "R":{}}
        self.__ruta = None

    #setter ruta
    def setRuta(self, rut: str):
        self.__ruta = rut

    #metodo director, que construye las direcciones
    def MethodDirector(self):
        self.BuildDown()
        self.BuildUp()
        self.BuildLeft()
        self.BuildRight()

    def LlenaVectores(self, Ind: str, Beg: int, End: int) -> list:
        '''
        ***
        Metodo que llena un vector con la direccion de un Sprite
        Arguments:
            Ind (str): El nombre base de las imagenes
            Beg (int): El numero de imagen con que inicia
            End (int): El numero de imagen con que finaliza
        Return: Lista de rutas de las imagenes
        '''
        return ['Sprites/' + self.__ruta + '/' + Ind +'%d.gif' % it for it in range(Beg,End)]

    #constructor de las sprites hacia abajo
    def BuildDown(self):
        self._build["D"]["Dir"] = self.LlenaVectores("D", 0, 3)
        self._build["D"]["Atk"] = self.LlenaVectores("DA", 0, 3)
        self._build["D"]["Def"] = self.LlenaVectores("DD", 0, 3)

    #constructor de las sprites hacia arriba
    def BuildUp(self):
        self._build["U"]["Dir"] = self.LlenaVectores("U", 0, 3)
        self._build["U"]["Atk"] = self.LlenaVectores("UA", 0, 3)
        self._build["U"]["Def"] = self.LlenaVectores("UD", 0, 3)

    #constructor de las sprites hacia la izquierda
    def BuildLeft(self):
        self._build["L"]["Dir"] = self.LlenaVectores("L", 0, 3)
        self._build["L"]["Atk"] = self.LlenaVectores("LA", 0, 3)
        self._build["L"]["Def"] = self.LlenaVectores("LD", 0, 3)

    #constructor de las sprites hacia la derecha
    def BuildRight(self):
        self._build["R"]["Dir"] = self.LlenaVectores("R", 0, 3)
        self._build["R"]["Atk"] = self.LlenaVectores("RA", 0, 3)
        self._build["R"]["Def"] = self.LlenaVectores("RD", 0, 3)

#Constructor de sonidos
class BuildSonidos(Builder):

    def __init__(self):
        #inicializacion para Sonidos
        self._build = {"G": None}
        self.__ruta = None

    #setter ruta
    def setRuta(self, rut):
        self.__ruta = rut

    #metodo director, que construye todos los sonidos
    def MethodDirector(self):
        self.BuildGrunido()

    #constructor de sonidos de gruñidos
    def BuildGrunido(self):
        self._build["G"]='Efects/'+self.__ruta+'/'+'G.wav'

#pruebas del manejo de las clases
def main():
    #constructor de sprites
    buld=BuilderSprites()

    #se le settea la ruta
    buld.setRuta("Personajes/Prueba")

    #se llama al director para que genere los sprites
    buld.MethodDirector()

    #imprimir (easy-peasy)
    for keys in buld.getBuild():
        print(buld.getBuild()[keys][len(buld.getBuild()[keys])-1])
    pass

if __name__ == '__main__':
    main()

#-------------------------------------------------------------------------------
# Name:        módulo1
# Purpose:
#
# Author:      estudiantes
#
# Created:     21/02/2020
# Copyright:   (c) estudiantes 2020
# Licence:     <your licence>
#-------------------------------------------------------------------------------

class StatePersonaje:
    _dir = None

    def __init__(self, pers):
        self._observador = pers
        self._observador.images = self._observador.getSprites()[self._dir]["Dir"]

    def getDir(self):
        return self._dir

    def getRHand(self):
        pass

    def getLHand(self):
        pass

    def draw(self):
        pass

class StatePersD(StatePersonaje):
    _dir = "D"

    def getRHand(self) -> list:
        if self._observador.ind == 0:
            return [5, 40]
        elif self._observador.ind <= self._observador.getVelocidadPaso():
            return [7, 40]
        else:
            return [5, 36]
        return[0,0]

    def getLHand(self) -> list:
        if self._observador.ind == 0:
            return [32, 40]
        elif self._observador.ind <= self._observador.getVelocidadPaso():
            return [32, 36]
        else:
            return [30, 40]
        return[0,0]

    def draw(self, marco):
        marco.blit(self._observador.image, self._observador.rect)
        if 'RH' in self._observador.getEquipamento().keys() and self._observador.getEquipo('RH'):
            self._observador.getEquipo("RH").draw(marco)
        if 'LH' in self._observador.getEquipamento().keys() and self._observador.getEquipo('LH'):
            self._observador.getEquipo("LH").draw(marco)

class StatePersU(StatePersonaje):
    _dir = "U"

    def getRHand(self) -> list:
        if self._observador.ind == 0:
            return [32, 40]
        elif self._observador.ind <= self._observador.getVelocidadPaso():
            return [33, 34]
        else:
            return [30, 40]

    def getLHand(self) -> list:
        if self._observador.ind == 0:
            return [5, 40]
        elif self._observador.ind <= self._observador.getVelocidadPaso():
            return [7, 40]
        else:
            return [5, 34]

    def draw(self, marco):
        if 'LH' in self._observador.getEquipamento().keys() and self._observador.getEquipo('LH'):
            self._observador.getEquipo("LH").draw(marco)
        if 'RH' in self._observador.getEquipamento().keys() and self._observador.getEquipo('RH'):
            self._observador.getEquipo("RH").draw(marco)
        marco.blit(self._observador.image, self._observador.rect)

class StatePersL(StatePersonaje):
    _dir = "L"

    def getRHand(self) -> list:
        if self._observador.ind == 0:
            return [16, 41]
        elif self._observador.ind <= self._observador.getVelocidadPaso():
            return [23, 42]
        else:
            return [14, 40]

    def getLHand(self) -> list:
        if self._observador.ind == 0:
            return [16, 41]
        elif self._observador.ind <= self._observador.getVelocidadPaso():
            return [13, 41]
        else:
            return [20, 43]

    def draw(self, marco):
        if 'RH' in self._observador.getEquipamento().keys() and self._observador.getEquipo('RH'):
            self._observador.getEquipo("RH").draw(marco)
        marco.blit(self._observador.image, self._observador.rect)
        if 'LH' in self._observador.getEquipamento().keys() and self._observador.getEquipo('LH'):
            self._observador.getEquipo("LH").draw(marco)

class StatePersR(StatePersonaje):
    _dir = "R"

    def getRHand(self) -> list:
        if self._observador.ind == 0:
            return [22, 41]
        elif self._observador.ind <= self._observador.getVelocidadPaso():
            return [18, 43]
        else:
            return [24, 41]

    def getLHand(self) -> list:
        if self._observador.ind == 0:
            return [21, 41]
        elif self._observador.ind <= self._observador.getVelocidadPaso():
            return [25, 41]
        else:
            return [17, 42]

    def draw(self, marco):
        if 'LH' in self._observador.getEquipamento().keys() and self._observador.getEquipo('LH'):
            self._observador.getEquipo("LH").draw(marco)
        marco.blit(self._observador.image, self._observador.rect)
        if 'RH' in self._observador.getEquipamento().keys() and self._observador.getEquipo('RH'):
            self._observador.getEquipo("RH").draw(marco)

def main():
    pass

if __name__ == '__main__':
    main()

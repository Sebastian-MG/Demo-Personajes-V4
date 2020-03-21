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

from enum import Enum

class TiposPersonajes(Enum):
    MAGO = "Mago"
    CABALLERO = "Caballero"
    ORCO = "Orco"
    ALDEANO = "Aldeano"
    TROLL = "Troll"

def main():
    for tip in TiposPersonajes:
        print(tip.value)
    pass

if __name__ == '__main__':
    main()

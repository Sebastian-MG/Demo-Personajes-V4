#-------------------------------------------------------------------------------
# Name:        módulo1
# Purpose:
#
# Author:      lenovo
#
# Created:     30/10/2019
# Copyright:   (c) lenovo 2019
# Licence:     <your licence>
#-------------------------------------------------------------------------------

import Game
from Tipos import *

def main():
    tips = [tip.name for tip in TiposPersonajes]
    print("Digite uno de las siguientes clases:")
    for tip in tips:
        print("-" + tip.capitalize())
    while True:
        pers = input()
        if pers.upper() in tips:
            Game.main(SELECT_PLAYER = pers)
            break
    pass

if __name__ == '__main__':
    main()
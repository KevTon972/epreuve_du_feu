#!/usr/bin/env python3
#Créez un programme qui affiche un rectangle dans le terminal

import sys 

def carre(vertical, horizontal):
    
    i = 0

    while i < vertical:
        j = 0

        #definir la premiere colone
        if i == 0 and j == 0: print("o", end="")

        elif i == 1: print("|", end="")

        elif i == vertical-1: print("o", end="")

        while j < horizontal:

            # remplir la premiere et la derniere ligne
            if i == 0 and j >= 1 and j < horizontal-1 or i == vertical-1 and j >= 1 and j < horizontal-1: print("-", end="")

            #fermer la premiere et la derniere ligne
            elif i == 0 and j == horizontal-1 and horizontal > 1 or i == vertical-1 and j == horizontal-1 and horizontal > 1 : print("o")

            #remplir la deuxieme ligne
            elif i == 1 and j >= 1 and j < horizontal-1: print(" ", end="")

            #fermer la deuxieme ligne
            elif i == 1 and j == horizontal-1: print("|")

            j += 1    
        i += 1

largeur = sys.argv[1]
hauteur = sys.argv[2]
    

try:
    carre(int(hauteur), int(largeur))
except ValueError:

        print(" les arguments doivent etre des entiers")
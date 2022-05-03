#!/usr/bin/env python3

#Créez un programme qui reçoit une expression arithmétique dans une chaîne de caractères et en retourne le résultat après l’avoir calculé.
#Vous devez gérer les 5 opérateurs suivants : “+” pour l’addition, “-” pour la soustraction, “*” la multiplication, “/” la division et “%” le modulo.

import sys

def parenthese(chaine):

    for i in chaine:
                       
        liste = i.split()               #separer les elements de la chaine 

    liste = list(liste)
          
    for j in liste:
        
        if "(" in j : j = indice1 = liste.index(j)             # recuperer l'indice des parentheses

        elif ")" in j: indice2 = liste.index(j)
        
    liste[indice1], liste[indice2] = "1", "2"                  #retirer les parentheses
       
    indx3 = liste[indice1:indice2+1]

    indx3 = calcul_and_switch(indx3)                #calculer l'operation qui etait entre parenthese et mettre le resultat a la place
    
    indx3 = str(indx3[0])               #convertir indx3 en str

    liste[indice1] = indx3 
        
    del liste[indice1+1:indice2+1]

    return liste
        
def calcul_and_switch(lst):

    if len(lst) == 1 :return lst
   
    for l in range(len(lst)):               # la premiere boucle gere les operateurs "*,/,%" 

        if lst[l] == "/":

            indice = lst.index(lst[l-1])             #recuperer l'indice du premeir chiffre de l'operation
            
            resultat = int(lst[l-1]) // int(lst[l+1])
                       
            lst[indice] = resultat              #remplacer les  3 elements de l'operation par le resultat 

            del lst[indice+1:indice+3]
            
            break
                    
        elif lst[l] == "*":
                        
            indice = lst.index(lst[l-1])
            
            resultat = int(lst[l-1]) * int(lst[l+1])            
            
            lst[indice] = resultat

            del lst[indice+1:indice+3]

            break
                    
        elif lst[l] == "%":

            indice = lst.index(lst[l-1])
            
            resultat = int(lst[l-1]) % int(lst[l+1])
            
            lst[indice] = resultat

            del lst[indice+1:indice+3]

            break

    for l in range(len(lst)):               #la deuxieme boucle gere les operateurs "+,-"

        if lst[l] == "-":
            
            indice = lst.index(lst[l-1])
            
            resultat = int(lst[l-1]) - int(lst[l+1])

            lst[indice] = resultat

            del lst[indice+1:indice+3]

            break
            
        elif lst[l] == "+":

            indice = lst.index(lst[l-1])
            
            resultat = int(lst[l-1]) + int(lst[l+1])
            
            lst[indice] = resultat

            del lst[indice+1:indice+3]

            break
            
    return calcul_and_switch(lst)
             
arg = sys.argv[1:]

sans_parenthese = parenthese(arg)

result = calcul_and_switch(sans_parenthese)

print(result[0])
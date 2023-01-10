def affichePuissance(nb,puissance,dernier):
    if puissance>1:
        print(nb,"^",puissance,end=" ")
    else:
        print(nb,end=" ")
    if not dernier:
        print("*",end=" ")

nombre = int(input("Entrez un nombre: "))

diviseur = 2                # diviseur de départ
print(nombre,"=", end=" ")  # on affiche le début de la décomposition eg "12 = "
precedentDiviseur = 0       # diviseur précédent (pour savoir si on doit afficher le "^")
compteurPuissance = 1       # compteur de puissance
while nombre != 1:          # tant que l'on n'a pas fini la décomposition
    if nombre % diviseur == 0:  # si le diviseur est un diviseur de nombre
        if diviseur == precedentDiviseur: # si le diviseur est le même que le précédent
            compteurPuissance = compteurPuissance + 1   
        else:            # si le diviseur est différent du précédent
            if precedentDiviseur != 0:
                affichePuissance(precedentDiviseur,compteurPuissance,False) # on affiche le diviseur et sa puissance
            precedentDiviseur = diviseur # on met à jour le diviseur précédent
            compteurPuissance = 1   # on remet le compteur de puissance à 1
        nombre = nombre / diviseur
    else:
        diviseur = diviseur + 1
affichePuissance(precedentDiviseur,compteurPuissance,True) # on affiche le dernier diviseur et sa puissance
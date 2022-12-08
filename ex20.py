##
# Tri à bulles d'un tableau d'entiers
#

import numpy

tableau = numpy.array([5,7,6,2,1,8,9,4,7])

changement = True
while changement:
    changement = False
    for i in range(len(tableau)-1):
        if (tableau[i] > tableau[i+1]):
            temp = tableau[i]
            tableau[i] = tableau[i+1]
            tableau[i+1] = temp
            changement = True

print(tableau)
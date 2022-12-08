##
# Somme de deux matrices
#

import numpy

mat1 = numpy.array([[1,2,3],[4,5,6]])
mat2 = numpy.array([[5,1,2],[3,4,7]])
somme = numpy.zeros((2,3))

for ligne in range(len(mat1)):
    for colonne in range(len(mat2[0])):
        somme[ligne,colonne] = mat1[ligne,colonne] + mat2[ligne,colonne]

print(somme)
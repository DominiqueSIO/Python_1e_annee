##
# Produit de deux matrices
#

import numpy

mat1 = numpy.array([[1,2,3],[4,5,6]])
mat2 = numpy.array([[5,1],[3,4],[4,2]])
produit = numpy.zeros((2,2))

for ligne in range(len(mat1)):
    for colonne in range(len(mat2[0])):
        for k in range(len(mat2)):
            produit[ligne,colonne] += mat1[ligne,k]*mat2[k,colonne]

print(produit)
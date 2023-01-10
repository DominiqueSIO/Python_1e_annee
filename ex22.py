import math

def isPrime(n):
    i = 2
    while i<=math.sqrt(n):
        if n%i==0:
            return False
        i+=1
    return True

nb = int(input("Donnez un nombre : "))
if isPrime(nb):
    print("Il est premier")
else:
    print("Il n'est pas premier")
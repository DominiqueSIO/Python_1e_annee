import math

def isPrime(n):
    i = 2
    while i<=math.sqrt(n):
        if n%i==0:
            return False
        i+=1
    return True

nb = int(input("Combien de nombres premiers : "))

count = 0
i = 2

while count<nb:
    if isPrime(i):
        print(i)
        count+=1
    i+=1
#Fonction binome#

n = int(input("Entrer un entier n: "))
p = int(input("Entrer un entier p: "))

def fact(N):
    facto=1
    for i in range(1,N+1):
        facto= i*facto
    return facto

def binom(n,p):
    if p > n:
        return 0
    elif p==0 or p==n:
        return 1
    else:
        return fact(n)//fact(p)*fact(n-p)

print(binom(n,p))

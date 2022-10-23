N = int(input("Entrez un entier"))

def fact(N):
    facto=1
    for i in range(1,N+1):
        facto= i*facto
    return facto
print("N!=",fact(N))



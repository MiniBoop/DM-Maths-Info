#Triangle de Pascal#

N=int(input("Entrez un entier: "))

def fact(N):
    facto=1
    for i in range(1,N+1):
        facto= i*facto
    return facto

def TrianglePascal(N):
    for i in range(N+1):
        for j in range(N-i+1):
            print()
        for j in range(i+1):
            print(fact(i)//(fact(j)*fact(i-j)),end=" ")
print(TrianglePascal(N))
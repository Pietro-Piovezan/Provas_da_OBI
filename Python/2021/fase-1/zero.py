numero_maximo_linhas = 11
numeros = []
N = int(input())
for i in range(N):
    x = int(input())
    if x == 0:
        numeros.pop()
    else:
        numeros.append(x)
print(sum(numeros))
numero_maximo_amigos = 100
vacuo = [False] * numero_maximo_amigos
tempo = [0] * numero_maximo_amigos


    
n = int(input())
for _ in range(n):
    evento, X = input().split()
    X = int(X)

    if evento == 'R':
        vacuo[X] = True
        for i in range(numero_maximo_amigos):
            if vacuo[i]:
                tempo[i] += 1
    
    if evento == 'E':
        vacuo[X] = False
        for i in range(numero_maximo_amigos):
            if vacuo[i]:
                tempo[i] += 1
    if evento == 'T':
        for i in range(numero_maximo_amigos):
            if vacuo[i]:
                tempo[i] += X - 1



for i in range(numero_maximo_amigos):
    if tempo[i] > 0:
        if vacuo[i]:
            print(i, -1)
        else:
            print(i, tempo[i])

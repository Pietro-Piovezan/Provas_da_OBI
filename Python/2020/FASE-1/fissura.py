N, F = map(int, input().split())
matriz = [list(input()) for _ in range(N)]
# print(matriz)

matriz_str = (''.join(''.join(sublista) for sublista in matriz))
# print(matriz_str)


def cord(n, N):
    if n >= N:
        x = n // N
    else:
        x = 0
    if x > 0:
        y = n -  x * N 
    else:
        y = n
    return(x, y)


for n in range(len(matriz_str)):

    x, y = cord(n, N)
    
    if int(matriz[x][y]) <= F:
        matriz[x][y] = '_'
    else:
        continue

for _ in range(len(matriz_str)):
    for n in range(len(matriz_str)):

        x, y = cord(n, N)

        if int(matriz_str[n]) <= F:
            matriz[0][0] = '*'

        if matriz[x][y] == '_':
            if y >= 1:
                if matriz[x][y - 1] == '*':
                    matriz[x][y] = '*'
            if y < N - 1:
                if matriz[x][y + 1] == '*':
                    matriz[x][y] = '*'
            if x >= 1:
                if matriz[x - 1][y] == '*':
                    matriz[x][y] = '*'
            if x < N -1:
                if matriz[x + 1][y] == '*':
                    matriz[x][y] = '*'

for n in range(len(matriz_str)):
    x, y = cord(n, N)
    if matriz[x][y] != '_':
        print(matriz[x][y], end='')
    else:
        print(matriz_str[n], end='')
    if y == N - 1:
        print('')

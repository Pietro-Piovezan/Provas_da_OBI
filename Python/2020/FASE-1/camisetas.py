maximo_camisetas = 1000
camisas_p = [False] * maximo_camisetas
camisas_m = [False] * maximo_camisetas
camisas = []

N = int(input())
t = input()

camisas = t.split()

P = int(input())
M = int(input())

for i, n in zip(camisas, range(N)):
    if i == '1':
        camisas_p[n] = 1
    elif i == '2':
        camisas_m[n] = 1

if sum(camisas_p) == P:
    if sum(camisas_m) == M:
        print('S')
    else:
        print('N')
else:
    print('N')

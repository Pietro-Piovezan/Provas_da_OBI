alfabeto = ["a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m", "n", "o", "p", "q", "r", "s", "t", "u", "v", "x", "z"]
consoantes = ["b", "c", "d", "f", "g", "h", "i", "j", "k", "m", "n", "p", "q", "r", "s", "t", "v", "x", "z"]
vogais = ["a", "e", "i", "o", "u"] 
P = input()
nova_palavra = ''
for letra in P:
    if letra not in vogais:
        nova_palavra += letra
        posicao = alfabeto.index(letra) 
        distancia_a = abs(posicao - alfabeto.index('a'))
        distancia_e = abs(posicao - alfabeto.index('e'))
        distancia_i = abs(posicao - alfabeto.index('i'))
        distancia_o = abs(posicao - alfabeto.index('o'))
        distancia_u = abs(posicao - alfabeto.index('u'))
        if distancia_a <= distancia_e and distancia_a < distancia_i and distancia_a < distancia_o and distancia_a < distancia_u:
            vogal = 'a'
        elif distancia_e <= distancia_i and distancia_e < distancia_o and distancia_a < distancia_u:
            vogal = 'e'
        elif distancia_i <= distancia_o and distancia_i < distancia_u:
            vogal = 'i'
        elif distancia_o <= distancia_u: 
            vogal = 'o'
        else:
            vogal = 'u'

        nova_palavra += vogal

        
        if letra != 'z':
            nova_palavra += consoantes[int(consoantes.index(letra)) + 1]
        else: 
            nova_palavra += 'z'
    else:
        nova_palavra += letra
print(nova_palavra)
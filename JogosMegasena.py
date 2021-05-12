from random import randint
lista = list()
jogos = list()

quantidade = int(input('Quantos jogos você quer que seja sorteado?: '))
total = 1

while total <= quantidade:
    cont = 0
    while True:
        num = randint(1, 60)
        if num not in lista:
            lista.append(num)
            cont += 1
            if cont >= 6:
                break
    lista.sort()
    jogos.append(lista[:])
    lista.clear()
    total += 1

for i, lista in enumerate(jogos):
    print(f'Jogo {i+1}: {lista}')
import random

with open('lista_de_palavras.txt', 'r') as f:
    palavras = f.readlines()

palavra = random.choice(palavras)[:-1]

erros_permitidos = 6
tentativas = []
fim = False

while not fim:
    for letra in palavra:
        if letra.lower() in tentativas:
            print(letra, end=" ")
        else:
            print("_", end=" ")
    print("")

    tentativa = str(input(f'Tentativas restantes {erros_permitidos}, próxima letra: '))
    tentativas.append(tentativa.lower())
    if tentativa.lower() not in palavra.lower():
        erros_permitidos -= 1
        if erros_permitidos == 0:
            break

    fim = True
    for letra in palavra:
        if letra.lower() not in tentativas:
            fim = False

if fim:
    print(f'Você acertou a palavra!!! A palavra era {palavra}')
else:
    print(f'Game Over!!! A palavra era {palavra}')

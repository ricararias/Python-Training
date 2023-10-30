import random

def sorteo():
    numero_min = 1
    numero_max = 6
    numero = random(numero_min, numero_max)
    return numero

while True:
    jogadores = input("Quantos jogadores? (2 - 4) ")
    if jogadores.isdigit():
        jogadores = int(jogadores)
        if 2<= jogadores <=4:
            break
        else:
            print("digite um numero entre 2 e 4")
    else:
        print("Formato invalido")


pontos = [0 for index_jogador in range(jogadores)]

print(pontos)


















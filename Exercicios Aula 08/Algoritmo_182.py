# Entrar com 10 números e imprimir a metade de cada número.
from os import system
system('cls')


for i in range(1, 11):
    numero = float(input("Digite um numero"))
    metade = numero / 2
    print(f'A metade de {numero} é {metade}')

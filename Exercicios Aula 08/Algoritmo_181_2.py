# Criar um algoritmo que imprima todos os números de 1 até 100 e a soma deles.
from os import system
system('cls')

soma = 0

for i in range(1, 101):
    soma += i
    if i == 1:
        print(f'{i} = {soma}')
    else:
        print(f'{soma - i} + {i} = {soma}')

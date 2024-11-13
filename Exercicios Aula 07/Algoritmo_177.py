# Imprimir os múltiplos de 5, no intervalo de 1 até 500
from os import system
system('cls')

i = 1

for i in range(1,501):
    if (i % 5 == 0):
        print(f'Os múltiplos de 5 são: {i}')
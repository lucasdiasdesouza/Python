# Imprimir os 100 primeiros pares
from os import system
system('cls')

i = 1

for i in range(1,101):
    if(i %2 ==0):
        print(f'Números pares: {i}')
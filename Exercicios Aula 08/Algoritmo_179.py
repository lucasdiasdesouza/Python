# Criar um algoritmo que imprima os numeros pares no intervalo de 1 a 600
from os import system
system('cls')

i = 1

for i in range(1,601):
    if(i % 2 == 0):
        print(f'{i}')
from os import system
system('cls')
import math

# Ler um número inteiro de 3 casas decimais e imprimir se o algarismo da casa das
# centenas é par ou ímpar.

numero = int(input("número de 3 algarismos: "))

if (numero % 2 ==0 ):
    print("Algorismos da centena é par")
else:
    print("Algorismos da centena é impar")
from os import system
system('cls')
import math
# Ler um número inteiro de 4 casas e imprimir se é ou não múltiplo de quatro o
# número formado pelos algarismos que estão nas casas das unidades de milhar e das
# casas das unidades de milhar e das centenas.

numero = int(input("número de 4 algarismos: "))

if (numero % 4 ==0):
    print("É múltiplo de 4")
else:
    print("Não é múltiplo de 4")
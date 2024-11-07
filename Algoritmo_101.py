from os import system
system('cls')
import math
# Construir um algoritmo que indique se o número digitado está 
# compreendido entre 20 e 90 ou não.

numero = int(input("Digite um número: "))

if (numero > 20 and numero <90):
    print("Dentro dos números 20 ao 90")
else:
    print("Não está dentro dos números 20 ao 90")
    
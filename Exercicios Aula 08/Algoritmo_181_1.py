# Criar um algoritmo que imprima todos os números de 1 até 100 e a soma deles.
from os import system
system('cls')

i = 1
soma = 0

for i in range(i,101):
    # pega o numero de i e soma com o proximo, exemplo resultado 1=1, o 1 do resultado 
    # soma com o 2 adiante = 3
    soma += i
    print(f'{i} = {soma}')
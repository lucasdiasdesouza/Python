# Criar uma lista de números de 10 a 20 e imprimir.
from os import system
system('cls')

numeros = []

for i in range(10, 21):
    numeros.append(i)  # Adiciona o número à lista
    print(i)  # Imprime o número durante o loop

# Após o loop, imprime a lista inteira
print("Lista completa de números de 10 a 20:", numeros)
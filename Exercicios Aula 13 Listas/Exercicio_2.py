# Acessar o ultimo elemento da lista, acesse e imprima o ultimo elemento da lista.
from os import system
system('cls')

frutas = ["banana","maça","laranja","manga"]
print(frutas)

print("=="*30)

indice = frutas.index("manga") # index: mostrar posição na lista
print(indice)
print(frutas[-1])
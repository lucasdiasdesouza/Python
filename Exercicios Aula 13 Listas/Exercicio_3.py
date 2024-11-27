# Modificar um elemento da lista. Alterar o segundo item para "kiwi"
from os import system
system('cls')

frutas = ["banana","maça", "laranja"]
print(frutas)
frutas.pop(1)
frutas.insert(1,"kiwi")

print(frutas[0])
print(frutas[1])
print(frutas[2])
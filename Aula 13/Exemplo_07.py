from os import system
system('cls')

frutas = ["maça","banana","laranja"]
print(frutas)
indice = frutas.index("laranja") # index: serve para mostrar a posição da palavra
frutas.pop(2) # pop: exclue o item na posição que ele estiver
print(frutas)

print("=="*30)

frutas = ["maça","banana","laranja"]
print(frutas)
remover = input("Digite a palavra para remover: ")
indice = frutas.index(remover) 
frutas.pop(indice) 
print(frutas)
print("=="*30)
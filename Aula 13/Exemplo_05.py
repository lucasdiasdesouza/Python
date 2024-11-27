from os import system
system('cls')

frutas = ["maça","banana","laranja"]
print(frutas)
print("=="*30)

frutas.insert(1, "Kiwi") # insert é para inserir algo na tabela e empurrar os outros para tras

print(frutas)
print("=="*30)

frutas.insert(4, "Morango")

print(frutas)
print("=="*30)

frutas.insert(10,"Pitanga")

print(frutas)
print("=="*30)

print(frutas[5])
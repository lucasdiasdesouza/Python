from os import system
system('cls')

frutas = ["maça","banana","laranja"]
print(frutas)
print("=="*30)
frutas.append("Kiwi")
print(frutas)
print("=="*30)
frutas.append("Pitanga")
print(frutas)
print("=="*30)
aux = input("Digite uma fruta: ")
frutas.append(aux)
print(frutas)
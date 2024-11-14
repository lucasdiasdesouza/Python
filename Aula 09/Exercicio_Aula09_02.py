from os import system
system('cls')

sexo = input("Digite o genero: ")

if(sexo=="feminino"):
    genero = sexo.upper()
    print(genero)
elif(sexo=="Masculino"):
    genero = sexo.lower()
    print(genero)
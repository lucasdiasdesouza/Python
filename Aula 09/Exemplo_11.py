from os import system
system('cls')

lista = [1,2,3] # contagem começa do 0, é 1(0),2(1),3(2).

try:
    print(lista[2])
except IndexError:
    print("Erro: Índice fora do intervalo")
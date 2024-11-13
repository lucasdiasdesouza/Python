from os import system
system('cls')
import time

cont = 0

while (True):
    num = int(input("Digite um número ou 0 para sair: "))
    if num == 0:
        break
    #cont == cont +1
    cont +=1
print(f'Você digitou {cont} numeros')
    
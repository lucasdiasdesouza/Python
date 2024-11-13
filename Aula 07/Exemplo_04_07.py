from os import system
system('cls')
import time

i=1

while (i<=10):
    if (i % 2 == 0):
        print(f'{i} é um número par')
    else:
        print(f'{i} é um número impar')
    i+=1
print("Fim do loop")
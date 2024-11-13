from os import system
system('cls')
import time

i= 1
soma = 0

while (i<=5):
    #soma  = soma +i
    soma +=i
    print("volta: ",i)
    i+=1
print("Soma dos numeros: ",soma)
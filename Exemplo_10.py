from os import system
system('cls')
import time

soma =0

for i in range(1,6):
    #soma recebe soma + i
    soma+=i
print(f'soma total dos numeros: {soma}')
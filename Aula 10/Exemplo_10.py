from os import system
system('cls')

# Definindo as funções
def fibonacci(n):
    if n <=1:
        return n
    else:
        return fibonacci(n-1)+fibonacci(n-2)
    
print(fibonacci(6))
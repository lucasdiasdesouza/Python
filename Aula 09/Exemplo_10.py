from os import system
system('cls')

try:
    arquivo = open("arquivo.txt","r")
    print(arquivo.read())
except FileNotFoundError:
    print("Erro: Arquivo não encontrado")
finally:
    print("Fechando o arquivo.")
    arquivo.close()
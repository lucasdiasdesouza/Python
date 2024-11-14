from os import system
system('cls')

try:
    x = int(input("Digite um número: ")) # ValueError = digitou um valor que não é um número
    y = 10/x # ZeroDivisionError = colocar o numero 0 da erro, não da para dividir por 0
    print(y)
except ValueError:
    print("Erro: Você digitou um número inválido")
except ZeroDivisionError:
    print("Erro: Não é possivel dividir por zero")
else:
    print("Operação concluída com sucesso!")
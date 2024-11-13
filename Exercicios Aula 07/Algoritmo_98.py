from os import system
system('cls')
import math
# A prefeitura do Rio de Janeiro abriu uma linha de crédito para os funcionários
# estatutários. O valor máximo da prestação não poderá ultrapassar 30% do salário
# bruto Fazer um algoritmo que permita entrar com o salário bruto e o valor da
# prestação e informar se o empréstimo pode ou não ser concedido.

salariob = float(input("Digite o sálario: "))

v_prestacao = float(input("Digite o valor da prestação: "))

if (v_prestacao <= 0.3 *salariob ):
    print("Empréstimo concedido")
else:
    print("Empréstimo negado")
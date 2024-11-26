from Calculadora import Calculo
import os
os.system('cls')

class Calculadora(Calculo):
    def __init__(self):
        self.total = 0
        
numero_01 = int(input("Digite um número: "))
numero_02 = int(input("Digite um número: "))
op = input("Digite a operação: ")
        

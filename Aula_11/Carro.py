from os import system
system('cls')
# Sempre que usar class começar com letra maiuscula
class Carro:
    # Primeira pergunta "O que tenho"
    # Método construtor da classe, ele inicializa os atributos da classe
    def __init__(self, modelo, cor):
        self.modelo = modelo
        self.cor = cor
        
    # O que faço
    # Método para exibir as informações sobre o carro
    def mostrarInfo(self):
        print(f"Modelo: {self.modelo}, cor: {self.cor}")
        
Fiat_Uno = Carro("Vivace", "Azul")
print(Fiat_Uno.modelo)
print(Fiat_Uno.cor)
Fiat_Uno.mostrarInfo()
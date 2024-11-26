from HerancaBasica_02 import Pessoa
import os
os.system('cls')

class Menina(Pessoa):
    def __init__(self, nome, idade,cpf,rg):
        super().__init__(nome, idade)
        self.cpf = cpf
        self.rg = rg
    def exibir(self):
        print(f'CPF: {self.cpf}, RG: {self.rg}')
        return super().exibir()
    
menina = Menina("Janaina", "15","9876654321","2589-98")
menina.exibir
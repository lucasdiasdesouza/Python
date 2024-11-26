import os
os.system('cls')

class Animal:
    def fazer_som(self):
        print("O animal fez um som")
        
class Gato(Animal):
    def fazer_som(self):
        print("O gato mia")
        
        
gato = Animal()
gato.fazer_som()
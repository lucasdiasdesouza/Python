from os import system
system('cls')
import time

class Bomba_02:
    def __init__(self):
        self.status = False
        
    def ligar(self, tempo: int):
        """Ligar a bomba por um determinado tempo(em segundos)."""
        if self.status:
            print("A bomba já está ligada.")
            return
        
        self.status = True
        print("Bomba ligada.")
        for segundos_restantes in range(tempo, 0, -1):
            print(f'Segundos restantes: {segundos_restantes}')
            time.sleep(1)
        self.desligar()
        
def desligar(self):
    """Desliga a bomba"""
    if not self.status:
        print("A bomba já está desligada")
        return
    
    self.status = False
    print("Bomba desligada")
    
#Classe usa Bomba

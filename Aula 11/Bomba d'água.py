from os import system
system('cls')

class Bomba_agua:
    def __init__(self, ligar, desligar):
        self.ligar = ligar
        self.desligar = desligar
        
    
status_ligado = True
status_desligado = False
    
if(status_ligado):
    print("Ligar")
else:
    print("Desligar")


    
    
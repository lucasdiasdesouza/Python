# Fórmula de juros compostos A = P*(1+R/N)^(N*T)
#



from os import system
system('cls')
import math

p = 16000 #(Valor Principal)
r = 0.05 # é juros por ano
n = 12 # (meses)
t = 30# anos

a = p*(1+r/n)**(n*t)
print(f'O valor final com juros compostos: {a:.2f}')
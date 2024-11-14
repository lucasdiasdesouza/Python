from os import system
system('cls')

texto = "Python é legal"
print(texto.startswith("Python")) # startwicth ve se termina com a palavra inicial que está ali dentro
print(texto.endswith("Legal")) # endwicth ve se termina com a palavra final que está ali dentro
print("é" in texto) # vai dizer se existe a palavra "é" no texto
print(texto.count("legal")) # Quantas vezes a palavra vai aparecer dentro da variavel
textoTrocado = texto.replace("legal", "top") # replace = troca de palavras
print(textoTrocado)
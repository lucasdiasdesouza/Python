from os import system
system('cls')
# Entrar com o ano de nascimento de uma pessoa e o ano atual. Imprimira idade da
# pessoa. Não se esqueça de verificar se o ano de nascimento é um ano válido.

an = int(input("Digite o ano de nascimento: "))
at = int(input("Digite o ano atual: "))
idade = at - an

if (an >=1980 and at <2025):
    print(f'Idade: {idade}')
elif (idade < 1980):
    print("Ano inválido")
else:
    print("")
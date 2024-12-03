from os import system
system('cls')

#Criando um dicionário
dicionario = {'nome':'João','idade': 21,'cidade':'São Paulo'}
print(dicionario)

#Consultando o valor do dicionario
print(dicionario['nome'])

#Alterar o valor de um dicionario
dicionario['idade'] = 30
print(dicionario)

#Adicionando uma nova chave no dicionario
dicionario['profissão']='engenheiro'
print(dicionario)

#Removendo um item de um dicionario
del dicionario['cidade']
print(dicionario)
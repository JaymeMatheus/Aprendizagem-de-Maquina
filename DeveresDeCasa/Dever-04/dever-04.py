import csv

dados = [
    ["Nome", "Idade"],
    ["Ana", 25],
    ["Bruno", 30],
    ["Carla", 22],
    ["Daniel", 28],
    ["Eduardo", 35]
]

with open("dados.csv", mode="w", newline="") as file:
    writer = csv.writer(file)
    writer.writerows(dados)

import csv

def ler_arquivo():
    with open("dados.csv", mode="r", newline="") as file:
        reader = csv.reader(file)
        dados = list(reader)[1:]  
    return dados

def pessoa_mais_velha(dados):
    return max(dados, key=lambda x: int(x[1]))  

dados = ler_arquivo()

nome_usuario = input("Digite um nome: ").capitalize()
encontrado = False

for pessoa in dados:
    nome, idade = pessoa
    if nome == nome_usuario:
        encontrado = True
        idade = int(idade)
        
        print(f"{nome} tem {idade} anos.")

        mais_velho = pessoa_mais_velha(dados)
        if pessoa == mais_velho:
            print(f"{nome} é a pessoa mais velha da lista.")
        else:
            print(f"{nome} não é a pessoa mais velha da lista.")
        break

if not encontrado:
    print(f"O nome {nome_usuario} não foi encontrado na lista.")

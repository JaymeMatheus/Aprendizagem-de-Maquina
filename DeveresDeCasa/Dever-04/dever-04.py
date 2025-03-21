import pandas as pd
import random

frutas = ["maçã", "banana", "laranja", "uva", "maçã", "melão", "mamão", "banana"]

quantidades = {}

for fruta in frutas:
    quantidade = random.randint(0, 100)
    nova_quantidade = min(quantidades.get(fruta, 0) + quantidade, 100)
    quantidades[fruta] = nova_quantidade

with open("minhas_frutas.txt", "w", encoding="utf-8-sig") as file:
    for fruta, quantidade in quantidades.items():
        file.write(f"{fruta},{quantidade}\n")

dados = pd.read_csv("minhas_frutas.txt", names=["Fruta", "Quantidade"], encoding="utf-8-sig")

print(dados)
import pandas as pd
import random

frutas = ["maçã", "banana", "laranja", "uva", "maçã", "melão", "mamão", "banana"]

set_frutas = list(set(frutas))

quantidades = {}
for fruta in frutas:
    quantidade = random.randint(0, 100)
    quantidades[fruta] = quantidades.get(fruta, 0) + quantidade


with open("minhas_frutas.txt", "w", encoding="utf-8-sig") as file:
    for fruta, quantidade in quantidades.items():
        file.write(f"{fruta},{quantidade}\n")


dados = pd.read_csv("minhas_frutas.txt", names=["Fruta", "Quantidade"], encoding="utf-8-sig")
dados = dados.groupby("Fruta", as_index=False).sum()

print(dados)

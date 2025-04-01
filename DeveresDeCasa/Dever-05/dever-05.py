import pandas as pd
from sklearn.tree import DecisionTreeClassifier

data = {
    'IMC': [18.3, 22.4, 25.1, 30.5, 32.0, 27.7, 35.3, 28.9, 23.2, 31.1],
    'Obeso': [False, False, False, True, True, False, True, False, False, True]
}

df = pd.DataFrame(data)

X = df[['IMC']]
y = df['Obeso']

model = DecisionTreeClassifier()
model.fit(X, y)

def predict_obesity(imc):
    prediction = model.predict(pd.DataFrame([[imc]], columns=['IMC']))
    return "É Obeso" if prediction[0] else "Nao é obeso"

imc_pergunta = float(input("Digite o IMC: "))

resultado = predict_obesity(imc_pergunta)

print(f"O IMC {imc_pergunta} {resultado}")

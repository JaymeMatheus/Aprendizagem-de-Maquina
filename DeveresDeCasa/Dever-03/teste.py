def obter_frase():
    while True:
        frase = input("Digite uma frase: ").strip()
        if frase:
            return frase
        print("Erro: A entrada não pode estar vazia. Tente novamente.")

def analisar_frase(frase):
    num_caracteres = len(frase)
    palavras = frase.split()
    num_palavras = len(palavras)
    palavra_mais_longa = max(palavras, key=len) if palavras else ""
    
    
    frase_invertida_caracteres = frase[::-1]
    frase_invertida_palavras = " ".join(reversed(palavras))
    frase_maiuscula = frase.upper()
    frase_minuscula = frase.lower()
    tupla_palavras = tuple(palavras)
    
    
    print("\n=== Análise da Frase ===")
    print(f"Número de caracteres: {num_caracteres}")
    print(f"Número de palavras: {num_palavras}")
    print(f"Palavra mais longa: {palavra_mais_longa}")
    print(f"Frase invertida por caracteres: {frase_invertida_caracteres}")
    print(f"Frase invertida por palavras: {frase_invertida_palavras}")
    print(f"Frase em maiúsculas: {frase_maiuscula}")
    print(f"Frase em minúsculas: {frase_minuscula}")
    print(f"Tupla de palavras: {tupla_palavras}")


frase_usuario = obter_frase()
analisar_frase(frase_usuario)


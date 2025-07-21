import random

def sortear_ingresso():
    return random.randint(1, 100)

numero_sorteado = sortear_ingresso()
print(f"O número sorteado é o {numero_sorteado}.")
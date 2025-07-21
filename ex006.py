numero = int(input("Digite um número inteiro positivo: "))

contador = 0
for i in range(numero + 1):
    if i % 2 == 0:
        contador += i

print(f"Soma dos número pares: {contador}")

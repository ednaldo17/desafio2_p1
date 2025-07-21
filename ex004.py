def maior_numero(num1, num2, num3):
    numeros = [num1, num2, num3]
    return max(numeros)

numeros = []
for i in range(3):
    numero = float(input(f"Informe o {i+1}º número: "))
    numeros.append(numero)

maior = maior_numero(numeros[0], numeros[1], numeros[2])
print(f"Maior número: {round(maior, 2)}")

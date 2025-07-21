frase = input("Digite uma frase: ")

contador_vogais = 0
for i in frase:
    if i in "aeiouAEIOU":
        contador_vogais += 1

print(f"A frase contém {contador_vogais} vogal/vogais.")

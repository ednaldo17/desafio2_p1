def imc():
    peso = float(input("Informe o peso (kg): "))
    altura = float(input("Informe a altura (m): "))

    if altura <= 0:
        print("Altura inválida. Tente novamente.")
        exit()
    
    return peso / altura ** 2

def calcula_imc(imc):
    if imc < 18.5:
        print("Baixo peso.")
    elif 18.5 <= imc <= 24.9:
        print("Peso normal.")
    elif 25 <= imc <= 29.9:
        print("Sobrepeso.")
    elif 30 <= imc <= 34.9:
        print("Obesidade grau I.")
    elif 35 <= imc <= 39.9:
        print("Obesidade grau II.")

imc_usuario = imc()
print(f"IMC: {imc_usuario:.2f}.")
calcula_imc(imc_usuario)

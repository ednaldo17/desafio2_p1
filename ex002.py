valor_total = float(input("Total da compra: R$ "))
valor_pago = float(input("Valor pago: R$ "))

if valor_total < valor_pago:
    troco = valor_pago - valor_total
    print(f"Troco: R$ {troco:.2f}.")
elif valor_total == valor_pago:
    print("Não há troco.")
else:
    restante = valor_total - valor_pago
    print(f"Falta pagar: R$ {restante:.2f}")

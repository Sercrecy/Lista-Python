#simulador de poupança--
aporte = float(input("Quanto voce vai depositar por mes "))
juros = float(input("Qual a taxa da poupança atual "))
meses = int(input("Por quantos meses voce vai investir "))
juros_decimal = juros/100
total = 0
for mes in range(1, meses +1):
    total = total + aporte
    total = total + (total * juros_decimal)
    print(f"Mes{mes}: Saldo Total = R${total}")
rint(f"Ao final de {mes} meses, voce tera o valor de R$:{total:.2f}")
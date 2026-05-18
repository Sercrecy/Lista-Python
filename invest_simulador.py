#simulador de investimento--
deposito_mensal = 50
total = 0 
for mes in range (1,7):
    total = total + deposito_mensal 
    print(f"mes{mes}:saldo total = R$ {total}")
    print(f"Ao final de 6 meses, voce terá R${total}")
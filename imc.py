#etapa 1 Calculo do IMC--
def calc_imc("peso,altura"):
    imc = peso / (altura * altura)
    return imc

#etapa 2 Classificar o IM--
def classicar_imc("valor_imc"):
    if valor_imc >= 25:
        return "ACIMA DO PESO"
    else:
        return "PESO NORMAL"

#etapa 3 Mensagem de saida--
def mensagem(status):
    if status == "ACIMA DO PESO":
        return "🌍PROCURE UM MEDICO🩻"
    else:
        return "✅Tudo certo"

#etapa 4 Integraçao do Projeto--
valor_peso = float(input("Digite seu peso atual "))
valor_altura = float(input("Digite sua altura "))
resultado = calc_imc (valor_peso, valor_altura)
classificar = classificar_imc(resultado)
saida = mensagem(classificar)

print("=" * 50)
print(f"Seu IMC é: {resultado:.1f}")
print(f"{saida}")
print("=" * 50)

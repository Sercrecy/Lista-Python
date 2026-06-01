#aluno1: Padronizar nome do filme 
def formatar (nome):
    return nome.upper()
#aluno2: Verificar de Idade 
def vericador_idade(idade)
if idade >= 18:
    return 'Autorizado'
    else:
        return 'Não Autorizado'
#Aluno3: Mensagem de Retorno
def gerar_mensagem(status):
   if status =="Autorizado":
     return "Tenha uma otima sessaão"
    else:
        return "Sentimos, mas voce nao tem idade minima"
#aluno4: Exercução do Algoritmo
filme_entrada = input("Digite o filme Escolhido")
idade_entrada = int(input("Digite sua Idade"))
nome_final = formatar (filme_entrada)
status_acesso = verificar_idade(idade_idade)
mensagem = gerar_mensagem(status_acesso)
print(f"\nFilme:{nome_final}")
print(f"status:{status_acesso}")
print(f"mensagem:{mensagem}")
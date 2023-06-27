"""
Iterando Strings com while
"""
#       12345678901234
nome = 'Maicon Douglas'
#      -43210987654321
tamanho_nome = len(nome)
print(nome)
print(tamanho_nome)

cont=0

while cont < tamanho_nome:
    
    letra=nome[cont]
    novo_nome=f'*{letra}'
    print(novo_nome)
    cont+=1
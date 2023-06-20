"""
Peça ao usuário para digitar seu nome
Peça ao usuário para digitar sua idade
Se nome e idade forem digitados:
    Exiba:
        Seu nome é {nome}
        Seu nome invertido é {nome invertido}
        seu nome contem (ou não) espaços
        Seu nome tem {n} letras
        A primeira letra do seu nome é {F_Letra}
        A última letra do seu nome é {L_letra}
Se nada for digitado em nome ou idade:
    exiba "Desculpe, você deixou campos vazios.
"""
nome=str(input('Digite seu nome: '))

idade=input('Agora, digite sua idade: ')

if not nome and not idade:
    print('Desculpe, você deixou os campos vazios.')
else:
    print(f'Seu nome é {nome}.')
    print(f'Seu nome invertido é {nome[::-1]}.')
    if ' ' in nome:
        print('Seu nome tem espaços.')
    else:
        print('Nome não tem espaços.')
    print('Seu nome tem' ,len(nome), 'letras')
    print('A primeira letra do seu nome é',nome[0:1])
    print('A última letra do seu nome é',nome[:-2:-1])

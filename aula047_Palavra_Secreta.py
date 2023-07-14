"""
Faça um jogo para o usuário adivinhar qual
a palavra secreta.
- Você vai propor uma palavra secreta
qualquer e vai dar a possibilidade para
o usuário digitar apenas uma letra.
- Quando o usuário digitar uma letra, você 
vai conferir se a letra digitada está
na palavra secreta.
    - Se a letra digitada estiver na
    palavra secreta; exiba a letra;
    - Se a letra digitada não estiver
    na palavra secreta; exiba *.
Faça a contagem de tentativas do seu
usuário.
"""
palavra= 'Abacate'.upper()
palavra_len= len(palavra)
letras_acertadas=''
print('\033[36mDESCUBRA A PALAVRA SECRETA')
while True:
    
    letra=input('\033[37mDigite UMA letra: ').upper()
    if len(letra) > 1:
        print('Tem mais de um caractere aqui!')
        continue

    if letra in palavra:
        letras_acertadas += letra
    
    for letras_secreta in palavra:
        if letras_secreta in letras_acertadas:
            print(letras_secreta)
        else:
            print('*')

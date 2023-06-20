
#Faça um programa que peça ao usuário para digitar um número inteiro,
#informe se este número é par ou ímpar. Caso o usuário não digite um número
#inteiro, informe que não é um número inteiro.
print('É PAR OU IMPAR?!?!')
try:
    num_choice= int(input('Digite um número para analizarmos: '))
    if num_choice %2 == 0:

        print('\033[32mSeu número escolhido é PAR!')
    else:
        print('\033[31mSeu número escolhido é IMPAR!')
except:
    print('Opção inválida! Escolha um número inteiro.')


#Faça um programa que pergunte a hora ao usuário e, baseando-se no horário 
#descrito, exiba a saudação apropriada. Ex. 
#Bom dia 0-11, Boa tarde 12-17 e Boa noite 18-23.
print('Olá, humano! Poderia me dizer que horas são?')
horas= int(input('Claro que posso!: '))
print(f'São {horas}horas, senhor robô')
if horas <= 11:
    print('Muito obrigado e tenha um bom dia!')
elif horas >= 12 and horas <= 17:
    print('Agradecido, tenha uma boa tarde!')
elif horas > 18 and horas <= 23:
    print('Obrigado e boa noite!')


#Faça um programa que peça o primeiro nome do usuário. Se o nome tiver 4 letras ou 
#menos escreva "Seu nome é curto"; se tiver entre 5 e 6 letras, escreva 
#"Seu nome é normal"; maior que 6 escreva "Seu nome é muito grande". 
print('Avaliador de tamanho de nomes')
nome= str(input('Digite seu primeiro nome: '))
size_name=(len(nome))
if size_name <=4:
    print('Seu nome é curto.')
if size_name >= 5 and size_name <=6:
    print('Seu nome é mediano')
if size_name > 6:
    print('Seu nome é muito longo!')
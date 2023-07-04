#Exercício Calculadora Guiada
#Adção #Subtração
#Divisão #Multiplicação
SAIR = 'N' #[S]im

while SAIR == 'N':
    try:
        print('Vamos Calcular!\n')
        #Adção #Subtração #Divisão #Multiplicação
        print('''\033[36m[+] Adição  | [-]Subtração |
[/] Divisão | [*]Multiplicação ''')
        operador=str(input('\n\033[37mEscolha um Operador: '))
        p_numero=int(input('Escolha o primeiro número: '))
        s_numero=int(input('Escolha o segundo número: '))
    
        if operador == '+':
            soma= p_numero + s_numero
            print(f'O resuldado da soma: {p_numero}{operador}{s_numero} é \033[32m{soma}')
        elif operador == '-':
            sub= p_numero - s_numero
            print(f'O resuldado da subtração: {p_numero}{operador}{s_numero} é \033[32m{sub}')
        elif operador == '/':
            div= p_numero / s_numero
            print(f'O resultado da divisão: {p_numero}{operador}{s_numero} é \033[32m{div}')
        elif operador == '*':
            mult= p_numero * s_numero
            print(f'O resultado da multiplicação: {p_numero}{operador}{s_numero} é \033[32m{mult}')
        elif operador != '+-*/':
            print('Isso não é um operador matemático!')
            continue
    except ValueError:
            print('Números inválidos. Tente novamente.\n')
            continue
    SAIR= input('Você quer sair?-[S]im [N]ão: ').upper()
    print('Saindo da Calculadora')

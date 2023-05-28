# Função print

#função  Argument\ sep="" muda o separador entre os prints.
print    (16, 78, sep="+") 

# Quebra de linha 
# A quebra de linha funciona com o argumento end="\n"
# Mas tmb pode ser
print('Quebre', end='$') #Neste caso o \n que é usando de forma escondida
#É substituído e a qeubra de linha não ocorre colocando  o $ no lugar da quebra e unindo as strings
print('a Linha', end='$$$\n')# Mas pode ser resolvido usando \n junto do novo argumento
#Separando as strings e mantendo o "$$$"
print('Aqui!!!')
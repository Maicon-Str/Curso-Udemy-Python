"""
Iterável -> str, range, etc (__iter__)
Iterador -> quem sabe entregar um valor por vez
next -> me entregue o próximo valor
iter -> me entregue seu iterador
"""
# for letra in texto
texto = 'Luiz'  # iterável

# iteratador = iter(texto)  # iterator
'''
 while True:
     try:
         letra = next(iteratador)
         print(letra)
     except StopIteration:
         break
'''
#O digitado acima é o que o For in faz abaixo sozinho.
for letra in texto:
    print(letra)
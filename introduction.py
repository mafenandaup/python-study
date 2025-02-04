import random

# BOOLEANOS EM PYTHON começam sempre com letra maiúscula

# FORMAS DE VARIÁVEIS INVÁLIDAS EM PYTHON

# 1idade   # Começa com um número
# nome-completo   # Usa um hífen em vez de um sublinhado
# if   # Palavra-chave reservada do Python

# OPERADORES LOGICOS; and, or, not

# 
# resultado_and = (a > 5) and (b < 5)   # True
# resultado_or = (a > 15) or (b < 5)   # True
# resultado_not = not (a > 5)   # False

idade = random.randint(1,27)
tamanho = 1.90

print('sua idade é de: ' ,idade, 'anos.')
if idade >= 18:
   print ("Você é maior de idade.")
else:
   print('você ainda é de menor')

   if (tamanho < 1.50):
      print('você é meio que um anão')
   elif(tamanho == 1.70):
         print('eh, tá na média')
   elif(tamanho> 1.70):
       print('quase um ciclope.')
      
contador = 0


while contador <= 5:

    print(contador)
    contador += 1
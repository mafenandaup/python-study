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


while contador <= 10:

    print(contador)
    contador += 1
    if (contador == 7):
        break

    
    frutas = ["maçã", "banana", "laranja"]

for fruta in frutas:
    print(fruta)

    # instruções continue e pass
    
    i = 0

    for i in range(10):
        i=+1
        if (i % 2 == 0):  #se o I for divisivel por dois, continua a printar, senão, passa
            continue
    print(i)
    
    # for i in range(5):
    # pass

    # TUPLAS EM PYTHON
    # ao contrario das listas, uma vez criadas, não podem ser modificadas

    minha_tupla = (1,2,67,2,2,4)
    
print (minha_tupla.index(2))   #devolve o índice da aparição do primeiro elemento na tupla

print (minha_tupla.index(2, 2))    # devolve o n° de vezes que o número aparece na tupla

#  FUNÇÕES DOS : em python (além dos blocos de código)

# 2. Fatiamento (Slicing)
# definir intervalos em listas, tuplas, strings ou outros objetos iteráveis.

# numeros = [0, 1, 2, 3, 4, 5]
# print(numeros[1:4])  # [1, 2, 3] - Elementos do índice 1 até 3
# print(numeros[:3])    # [0, 1, 2] - Do início até o índice 2
# print(numeros[3:])    # [3, 4, 5] - Do índice 3 até o final
# print(numeros[::-1])  # [5, 4, 3, 2, 1, 0] - Reverte a lista


# 3. Definição de Dicionários
# Em dicionários, os dois pontos separam as chaves de seus respectivos valores.

# pessoa = {"nome": "João", "idade": 25}
# print(pessoa["nome"])  # João
# print(pessoa["idade"])    # Imprime 25

# pessoa = {"nome": "João", "idade": 25, "cidade": "Madri"}


# print(pessoa.keys())    # Imprime dict_keys(["nome", "idade", "cidade"])
# print(pessoa.values())  # Imprime dict_values(["João", 25, "Madri"])
# print(pessoa.items())   # Imprime dict_items([("nome", "João"), ("idade", 25), ("cidade", "Madri")])


# pessoa.update({"profissao": "Engenheiro"})
# print(pessoa)  # Imprime {"nome": "João", "idade": 25, "cidade": "Madri", "profissao": "Engenheiro"}


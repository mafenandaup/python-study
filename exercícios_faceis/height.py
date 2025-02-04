import random

user_altura = float(input("Informe qual sua altura e te direi se você é alto ou não"))

if ((user_altura<1.40) and (user_altura>1.20)):
    print('uau, você é beeeeem anão')
elif((user_altura>1.40) and (user_altura<1.80)):
    print('quase uma pessoa normal...se vc for um homem, ainda não')
elif((user_altura>1.80)):
    print('caralho, tu é um ciclope?')
else:
    print('não conseguimos configurar sua altura de alienigena')
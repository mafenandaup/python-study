numeros =[5,36,78,1,32,11,215,14,2]
num_menor = numeros[0]
num_maior = numeros[0]

for i in range (1, len(numeros), +1):
    if numeros[i] < numeros [i-1]:
        num_menor = numeros[i]
    if numeros[i] > num_maior:
        num_maior = numeros[i]


print('o menor número da lísta é ', num_menor, ' , e o maior é ', num_maior)
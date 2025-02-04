soma_pares = 0
for i in range(20):
    if(i % 2 == 0):  
        soma_pares += i  
        print('+', i)
        print(soma_pares)

print('A soma total dos números pares é', soma_pares)
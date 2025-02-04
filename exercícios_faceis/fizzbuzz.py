print('olá, bem vindo ao jogo "fizzbuzz!"')
print("eu imprimo fizz se o número for divisível por 3.")
print("buzz se for divisivel por 5")
print("\nfizbuzz se for divisivel pelos 2\n")


while True:  
    fizzbuzz = int(input('\nInsira um número (ou digite um valor negativo para encerrar): '))
    
    if fizzbuzz < 0:  
        break

    if(fizzbuzz%5 ==0):
        print("buzz!")
    elif(fizzbuzz%3 == 0):
         print("fizz!")
    elif((fizzbuzz % 5 ==0) and (fizzbuzz % 3 == 0)):
        print("fizzbuzz!")

print("O jogo acabou, obrigada por jogar!")
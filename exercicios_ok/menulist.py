itemlist = ["maria", "bola", "banana", "queijo", "12", 12]

print(itemlist)

opc = 0
while (opc !=4):
    print ("tecla 1: adiciona um item")
    print ("tecla 2: remove um item")
    print("tecla 3: vê se existe um item na lista")
    print("tecla 4: sair do menu")
    opc = input("escolha a função desejada:")
    if(opc<=0 or opc>4):
        print("Função inválida. tente novamente.")
    elif(opc == 1):
        item_input = input('digite um ítem para ser adicionado a lista')
        itemlist.append(item_input)
        print("Item adicionado com sucesso!")
        print("Lista atualizada:", itemlist)
    elif (opc == 2):
        item_input = input('digite o ítem a ser removido da lista')
        if item_input in itemlist:
            itemlist.remove(item_input)
            print("Item removido com sucesso!")
        else:
            print("Item não encontrado na lista.")
        print("Lista atualizada:", itemlist)
    elif (opc == 3):
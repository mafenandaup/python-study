itemlist = ["maria", "bola", "banana", "queijo", "12", 12]

print(itemlist)

opc = 0
while (opc !=4):
    print("LISTA TIPADA")
    print ("tecla 1: adiciona um item")
    print ("tecla 2: remove um item")
    print("tecla 3: vê se existe um item na lista")
    print("tecla 4: sair do menu")
  
    try:
        opc = int(input("Escolha a função desejada (1-4): "))
    except ValueError:
        print("Entrada inválida. Por favor, insira um número entre 1 e 4.")
        continue

    if opc < 1 or opc > 4:
        print("Função inválida. Tente novamente.")
    elif(opc == 1):
        item_input = input('digite um ítem para ser adicionado a lista: ')
        itemlist.append(item_input)
        print("Item adicionado com sucesso!")
        print("Lista atualizada:", itemlist)
    elif (opc == 2):
        item_input = input('digite o ítem a ser removido da lista: ')
        if item_input in itemlist:
            itemlist.remove(item_input)
            print("Item removido com sucesso!")
        else:
            print("Item não encontrado na lista.")
        print("Lista atualizada:", itemlist)
    elif (opc == 3):
         item_input = input('digite o ítem a ser verificado na lista: ')
         if item_input in itemlist:
            print(f"O item '{item_input}' está na lista.")
    else:
            print(f"O item '{item_input}' não está na lista.")

print("Saindo do menu. Até logo!")
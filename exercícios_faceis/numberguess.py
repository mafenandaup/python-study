import random

num_sorteado = random.randint(1, 35)


for chances in range(5, 0, -1):  # Começa em 5, vai até 1, decrementando de 1 em 1.
    num_diff = int(input("Estou pensando em um número entre 1 e 35. Você tem 5 chances para adivinhar."))
    
    if num_diff == num_sorteado:
        print("Parabéns! Você acertou o número!")
        break  # Sai do loop se acertar
    elif num_diff > num_sorteado:
        print("O número é menor do que isso.")
    else:
        print("O número é maior do que isso.")
    
    if chances > 1:
        print(f"Você ainda tem {chances - 1} chance(s).")
    else:
        print("Acabaram suas chances!")
        print(f"O número era {num_sorteado}. Melhor sorte na próxima vez!")
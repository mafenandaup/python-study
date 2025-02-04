frutas = ["maçã", "banana", "laranja"]

for index, fruta in enumerate(frutas):
    print(f"{fruta} ÍNDEX: {index}")

# ao inverso
print("\nAGORA AO INVERSO\n")
for index, fruta in enumerate(reversed(frutas)):
    print(f"{fruta} ÍNDEX INVERSO: {len(frutas) - 1 - index}")

# add uma fruta só
frutas.append("pera")
print("FRUTA ADICIONADA", frutas)  # Imprime ["maçã", "banana", "laranja", "pera"]

# uma fruta no index desejado
frutas.insert(1, "uva")
print("FRUTA ADD NO INDEX 1", frutas)  # Imprime ["maçã", "uva", "banana", "laranja", "pera"]

frutas.remove("banana")
print("FRUTA REMOVIDA", frutas)  # Imprime ["maçã", "uva", "laranja", "pera"]

fruta_removida = frutas.pop(2)  # Vai "pocar" a fruta no index 2.
print(frutas)  # Imprime ["maçã", "uva", "pera"]
print("FRUTA REMOVIDA", fruta_removida)  # Imprime "laranja"


frutas.sort()
print(frutas)  # Imprime ["maçã", "pera", "uva"]


frutas.reverse()
print(frutas)  # Imprime ["uva", "pera", "maçã"]

# add várias frutas
frutas.extend(["pera", "maçã", "laranja"])
print(frutas)  

# Imprimindo todos os elementos
for i in range(len(frutas)): 
    print(i)
    print(frutas[i])

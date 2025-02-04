nome_pessoa = input("\nMe informe qual seu nome e veremos se é um palíndromo: ").lower()
# coloca o nome em lowercase

# remove espaços do nome
nome_pessoa = nome_pessoa.replace(" ", "")

if nome_pessoa == nome_pessoa[::-1]:
    print(f"O nome {nome_pessoa} é um palíndromo!")
else:
    print(f"O nome {nome_pessoa} não é um palíndromo.")

# Imprimindo cada caractere do nome
for character in nome_pessoa:
    print(character)

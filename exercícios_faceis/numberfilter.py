# nova_lista = [expressão for elemento in sequência if condição]

numbers = [1,2,3,4,5,6,7,8]
even_numbers = [x for x in numbers if x % 2 == 0]
print(even_numbers)

odd_numbers = [x for x in numbers if x % 2 != 0]
print(odd_numbers)

quadrados_pares = [x ** 2 for x in numbers if x % 2 == 0]
print(quadrados_pares)
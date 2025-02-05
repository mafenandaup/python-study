num_list = [1,5,6,72,4,78,9]
results = 0

for i  in range (1, len(num_list), +1):
 results += num_list[i]
print(f"Soma parcial após adicionar {num_list[i]}: {results}")

print ('a soma final de todos os números é' , results)

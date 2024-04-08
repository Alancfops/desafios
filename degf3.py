def separate_numbers():
  numbers = list(range(21))

  pares = numbers[::2]
  impares = numbers[1::2]

  return pares, impares

pares, impares = separate_numbers()

print("Números pares: ", pares)
print("Números ímpares: ", impares) 
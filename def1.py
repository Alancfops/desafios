print("DESAfIO 1 - 1")
def numbers():
  list = [1, 2, 3, 4, 5]
  return list
for positon, element in enumerate(numbers()):
  print(f"Posicao :{positon}| Valor :{element}")

print("DESAFIO 1 - 2")
def numbers():
    list =[0, 1, 2, 3, 4, 5 , 6 ,7, 8, 9, 10]
    return list

for num in reversed(numbers()):
    print(num)

print("DESAFIO 1 - 3")
def note():
  notas = [6, 8, 4, 10]
  return notas
total  = sum(note())
print(f"A soma das notas e de: {total}")
media = total / 2
print(f"A media das notas e:{media}")

print("DESAFIO 2 - 4")
def ages():
  idades = [18,2 ,7, 98, 16, 20, 76, 34, 52, 64, 2 , 35, 22, 28, 10, 17,15, 19, 40, 41]
  return idades
print("A maior idade", max(ages()))
print("A menor idade", min(ages()))
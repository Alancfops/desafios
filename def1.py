print("Desafio 1-1")
def numbers():
    return list(range(1, 16))
for num in numbers():
    print(num)

print("Desafio 1-2")  
def numbers():
    return list(range(1, 16))
for num in numbers():    
    print(num)

print("Desafio 1-3")
def numbers():
    nums = list(range(1, 16))
    return nums

for num in numbers():
    if num % 2 == 0:
        print(num)    

print("Desafio 1-4")
def numbers():
    nums = list(range(1, 16))
    return nums

for num in numbers():
    if num % 2 != 0:
        print(num)

print("Desafio 1-5(Os multiplos dos 3 em conjunto)")        
def numbers():
    nums = list(range(1, 16))
    return nums

for num in numbers():
    if num % 2 == 0 and num % 3 == 0 and num % 4 == 0:
        print(num)

print("Desafio 1-5(Multiplos de cada um deles)")        
def numbers():
    nums = list(range(1, 16))
    return nums

for num in numbers():
    if num % 2 == 0:
        print(f"{num} é múltiplo de 2")
    if num % 3 == 0:
        print(f"{num} é múltiplo de 3")
    if num % 4 == 0:
        print(f"{num} é múltiplo de 4")

print("Desafio 1-6")
def numbers():
    nums = list(range(1, 16))
    return nums

for num in reversed(numbers()):
    print(num)

print("Desafio 1-7")
def numbers():
    nums1 = list(range(1, 16))
    nums2 = list(range(1, 16))
    return nums1, nums2

soma1 = sum(numbers()[0])
soma2 = sum(numbers()[1])

razao = soma1 / soma2

print("Lista 1:", numbers()[0])
print("Lista 2:", numbers()[1])
print("Razão:", round(razao, 2))
def criar_matriz():
    num = int(input("Digite o tamanho da matriz (n x n): "))
    matriz = [[0]*num for i in range(num)]
    for i in range(num):
        for j in range(num):
            matriz[i][j] = int(input(f"Digite o elemento [{i+1}][{j+1}]: "))
    return matriz

matriz = criar_matriz()

for i in range(len(matriz)):
    for j in range(len(matriz[i])):
        print(matriz[i][j], end=" ")
    print()

def criar_matriz2():
    num = int(input("Digite o tamanho da matriz (n x n): "))
    matriz = [[0]*num for i in range(num)]
    for i in range(num):
        for j in range(num):
            matriz[i][j] = int(input(f"Digite o elemento [{i+1}][{j+1}]: "))
    return matriz

matriz = criar_matriz2()

for i in range(len(matriz)):
    for j in range(len(matriz[i])):
        matriz[i][j] = matriz[i][j] * 2

for i in range(len(matriz)):
    for j in range(len(matriz[i])):
        print(matriz[i][j], end=" ")
    print()   
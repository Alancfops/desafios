def criar_matriz():
    n = int(input("Digite o tamanho da matriz (n x n): "))
    matriz = [[0]*n for _ in range(n)]
    for i in range(n):
        for j in range(n):
            matriz[i][j] = int(input(f"Digite o elemento [{i+1}][{j+1}]: "))
    return matriz

matriz = criar_matriz()

for i in range(len(matriz)):
    for j in range(len(matriz[i])):
        print(matriz[i][j], end=" ")
    print()
    
def criar_matriz2():
    n = int(input("Digite o tamanho da matriz (n x n): "))
    matriz = [[0]*n for _ in range(n)]
    for i in range(n):
        for j in range(n):
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
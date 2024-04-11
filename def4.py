def ler_notas():
    notas = []
    while True:
        nota = input("Digite uma nota (Fim para parar): ")
        if nota == "Fim":
            break
        nota = float(nota)
        notas.append(nota)
    return notas

notas = ler_notas()

# Mostra a quantidade de notas que foram lidas
print(f"\n{len(notas)} notas foram lidas.")

# Exibe todas as notas na ordem em que foram informadas
print("\nNotas na ordem em que foram informadas:")
for nota in notas:
    print(nota)

# Exibe todas as notas na ordem inversa à que foram informadas
print("\nNotas na ordem inversa à que foram informadas:")
for nota in reversed(notas):
    print(nota)

# Calcula e mostra a soma das notas
soma = sum(notas)
print(f"\nA soma das notas é: {soma:.2f}")

# Calcula e mostra a média das notas
media = soma / len(notas)
print(f"A média das notas é: {media:.2f}")

# Calcula e mostra a quantidade de notas acima da média calculada
acima_media = 0
for nota in notas:
    if nota > media:
        acima_media += 1
print(f"{acima_media} notas estão acima da média.")
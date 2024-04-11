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

print(f"\n{len(notas)} notas foram lidas.")

print("\nNotas na ordem em que foram informadas:")
for nota in notas:
    print(nota)

print("\nNotas na ordem inversa à que foram informadas:")
for nota in reversed(notas):
    print(nota)

soma = sum(notas)
print(f"\nA soma das notas é: {soma:.2f}")

media = soma / len(notas)
print(f"A média das notas é: {media:.2f}")

acima_media = 0
for nota in notas:
    if nota > media:
        acima_media += 1
print(f"{acima_media} notas estão acima da média.")
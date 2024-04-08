def calcular_nota(notas):
    if not notas:
        return "Nenhuma nota fornecida."

    media = sum(notas) / len(notas)
    return media

def note():
    notas = []
    while True:
        print(f"Notas (Digite 'fim' para finalizar):")
        nota = input()
        if nota == "fim":
            break
        else:
            try:
                nota = float(nota)
                notas.append(nota)
                media = calcular_nota(notas
            except ValueError:
                print("Entrada inválida. Por favor, digite apenas números.")

    if not notas:
        print("Nenhuma nota fornecida antes do encerramento.")

note()
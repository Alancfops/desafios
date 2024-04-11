print("DESAFIO 2 - 1")
def nums():
  lista = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 14, 16, 17, 18, 19, 20]
  pares = []
  impares = []
   
  for num in lista:
      if num % 2 == 0:
          pares.append(num)
      else:
          impares.append(num)
  
  print ("\nOs numeros do vetor sao:\n", pares,"\nOs numeros pares são:\n",impares)

nums()

def temperatura():
    meses = [
        "Janeiro",
        "Fevereiro",
        "Março",
        "Abril",
        "Maio",
        "Junho",
        "Julho",
        "Agosto",
        "Setembro",
        "Outubro",
        "Novembro",
        "Dezembro",
    ]
    temperaturas = []
    for i in range(12):
        temperaturas.append(
            float(input(f"Digite a temperatura de {meses[i]} em ºC: "))
        )

    media = sum(temperaturas) / 12
    print(f"\nA média das temperaturas foi {media:.2f}ºC")
    print("Meses com temperaturas acima da média: ")
    for i in range(12):
        if temperaturas[i] > media:
            print(f"{i+1} - {meses[i]} com {temperaturas[i]:.2f}ºC")

temperatura()
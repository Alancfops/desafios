import string

def interrogar():
    perguntas = ["Telefonou para a vítima?",
                 "Esteve no local do crime?",
                 "Mora perto da vítima?",
                 "Tinha dívidas com a vítima?",
                 "Já trabalhou com a vítima?"]

    respostas = []

    for pergunta in perguntas:
        resposta = input(pergunta + " (sim / não) ").lower()
        respostas.append(resposta)

    respostas = [resposta.capitalize() for resposta in respostas]

    qtd_respostas_positivas = sum(resposta == "Sim" for resposta in respostas)

    if qtd_respostas_positivas == 2:
        print("Suspeita")
    elif qtd_respostas_positivas >= 3 and qtd_respostas_positivas <= 4:
        print("Cúmplice")
    elif qtd_respostas_positivas == 5:
        print("Assassino")
    else:
        print("Inocente")

interrogar()
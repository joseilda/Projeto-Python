import random

decisao = input("Você gostaria de jogar o dado? ")

while decisao:
    decisao = decisao
    numero = random.randint(1, 6)

    if(decisao == "SIM"):
        print(f"O número que caiu foi: {numero}")
        decisao = input("Deseja jogar novamente (SIM OU NÃO)?.").upper()

    elif(decisao == "NÃO" or decisao =="NAO"):
        break

    else:
        print("Digite apenas SIM ou NÃO....")
        decisao = input("Deseja jogar novamente (SIM OU NÃO)? ").upper()

if decisao == "NÃO" or decisao == "NAO":
    print("Fim de Jogo! Volte Logo...")

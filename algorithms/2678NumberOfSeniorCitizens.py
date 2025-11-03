def countSeniors(details):

    # variaveis
    contador = 0
    string = ""
    idade = 0

    # percorre a lista
    for i in range(len(details)):
        # transforma a string nos indices 11 e 12 da string atual (idade)
        string = (details[i][11]) + (details[i][12])
        # transforma a string em int para verificar se é maior que 60
        idade = int(string)
        # se for maior que 60, incrementa o contador
        if idade > 60:
            contador += 1
        

    return contador
        






details = ["7868190130M7522","5303914400F9211","9273338290F4010"]
print(countSeniors(details))
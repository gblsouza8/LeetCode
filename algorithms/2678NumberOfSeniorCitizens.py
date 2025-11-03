def countSeniors(details):

    contador = 0
    string = ""
    idade = 0
    for i in range(len(details)):
        string = (details[i][11]) + (details[i][12])
        idade = int(string)
        if idade > 60:
            contador += 1
        



    return contador
        






details = ["7868190130M7522","5303914400F9211","9273338290F4010"]
print(countSeniors(details))
def countDigits(num):

    # versao em string de num
    numString = str(num)
    # variavel a ser incrementada a cada digito que dividir o numero
    contador = 0

    # percorre os digitos 
    for i in range(len(numString)):

        # se o numero for divisivel pelo digito atual, incrementa o contador
        if num % int(numString[i]) == 0:
            contador += 1



    # retorna o contador
    return contador




num = 7
print(countDigits(num))
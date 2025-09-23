def sumOfTheDigitsOfHarshadNumber(x):

    # converte x em string para poder percorrer os digitos
    string = str(x)
    # inicializa a variavel com a soma 
    soma = 0
    # percorre os digitos de x
    for i in range(len(string)):
        # soma os digitos 
        soma += int(string[i])
    
    # se x for divisivel por soma, retornará soma
    if x % soma == 0:
        return soma
    # senao, retorna -1
    else:
        return -1
        


x = 18
print(sumOfTheDigitsOfHarshadNumber(x))
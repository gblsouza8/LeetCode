def minimumSum(num):
    # declaração de variaveis
    menores = []
    numeros = []
    string = str(num)
    indice = 0
    menor = 0
    stringPar = ""
    stringImpar = ""

    # transforma os numeros em uma lista para poder manusea-los mais facilmente
    for i in range(len(string)):
        numeros.append(int(string[i]))


    # enquanto tiver algo na lista de numeros, procura o menor valor, adiciona na lista de menores e remove o indice de numeros
    while len(numeros) > 0:
        # reseta os valores das variaveis
        menor = numeros[0]
        indice = 0
        for i in range(len(numeros)):
            if numeros[i] < menor:
                menor = numeros[i]
                indice = i
        menores.append(menor)
        del numeros[indice]


    # pega os numeros em indices pares e impares (para garantir que os 2 menores valores sejam os valores decimais) e transforma em uma string para unir os digitos
    for i in range(len(menores)):
        if i % 2 == 0:
            stringPar += str(menores[i])
        else:
            stringImpar += str(menores[i])

    # retorna a soma dos valores formados
    return int(stringPar) + int(stringImpar)
            



num = 2932
print(minimumSum(num))
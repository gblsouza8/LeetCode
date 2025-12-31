def countBits(n):

    # lista que será retornada
    saida = []

    # percorre todos os valores entre 0 e n
    for i in range(n+1):

        # define que o quociente inicial é i
        quociente = i
        # inicializa/reseta as variaveis que serão usadas no loop
        resto = 0
        restos = []
        soma = 0
        # enquanto o quociente for maior que 0
        while quociente > 0:
            # pega o resto da divisão por 2
            resto = int(quociente%2)
            # quociente agora tem o valor dividido por 2
            quociente = int(quociente/2)
            # adiciona o resto em restos
            restos.append(resto)

        # após sair do laço while, realiza a soma de todos os digitos de restos (versão binária do numero)
        for i in range(len(restos)):
            soma += restos[i]

        # adiciona a soma dos digitos em saida
        saida.append(soma)

    # retorna saida após sair do laço for
    return saida



n = 5
print(countBits(n))
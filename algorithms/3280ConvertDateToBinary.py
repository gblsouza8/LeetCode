def convertDateToBinary(date):
    # Divide as datas a partir dos "-"
    numeros = date.split('-')
    # Incializa uma lista para ficar mais fácil de montar a string
    data = []
    # Inicializa a string para salvar os números binários
    string = ""
    # Inicializa a variável x que será usada nos cálculos
    x = 0


    # Laço que percorre os números
    for i in range(len(numeros)):
        # Define o valor de x como o indice atual de numeros(que foi separado anteriormente)
        x = int(numeros[i])
        # Enquanto x for maior que 0
        while int(x) > 0:
            # Irá adicionar na lista a sobra de x / 2 em formato de string
            data.append(str(int(x%2)))
            # Dividirá x por 2 para realizar o cálculo novamente
            x = int(x/2)


        # Percorre a lista ao contrário após x ser igual a 0
        for j in range(len(data) -1, -1, -1):
            # Adiciona na string os valores da lista ao contrário
            string += data[j]



        # Depois de sair do laço que percorre a lista, adiciona "-" na string e zera a lista para ir ao próximo número
        string += "-"
        data = []

    # Retorna a string sem o último digito para não terminar com "-" no final 
    return string[:-1]


date = "2080-02-29"
print((convertDateToBinary(date)))
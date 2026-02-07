def calPoints(operations):


    # lista que será usada para armazenar as mudanças
    lista = []
    # soma que será retornada
    soma = 0

    # percorre as operações
    for i in range(len(operations)):
        # se for +, soma as duas ultimas inseridas
        if operations[i] == "+":
            lista.append(int(lista[-1])+int(lista[-2]))

        # se for D, multiplica por 2 o ultimo valor inserido
        elif operations[i] == 'D':
            lista.append(int(lista[-1])*2)
        
        # se for C, apaga o ultimo valor inserido
        elif operations[i] == 'C':
            del lista[-1]

        # se não for nenhuma operação, insere o número na lista
        else:
            lista.append(int(operations[i]))

    # soma todos os valores da lista
    for i in range(len(lista)):
        soma += lista[i]

    # retorna a soma 
    return soma







operations = ["5","2","C","D","+"]
print(calPoints(operations))
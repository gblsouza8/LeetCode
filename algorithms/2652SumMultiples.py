def SumOfMultiples(n):


    # lista que irá armazenar os numeros que forem divisiveis
    lista = []
    # variavel que irá ser retornada após a soma dos numeros
    soma = 0
    # percorre de 1 até o n
    for i in range(1, n+1):
        # se for divisivel por 3, 5 ou 7 adiciona na lista
        if i % 3 == 0 or i % 5 == 0 or i % 7 == 0:
            lista.append(i)


    # soma todos os valores de lista
    for i in range(len(lista)):
        soma += lista[i]
    
    # retorna soma
    return soma





n = 7
print(SumOfMultiples(n))
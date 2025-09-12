def minElement(nums):

    # lista com as somas dos digitos em nums
    listaSomados = []
    # percorre nums
    for i in range(len(nums)):
        # transforma o indice atual em string para poder percorrer
        string = str(nums[i])
        # variavel soma que irá salvar a soma dos digitos do indice atual e reseta para 0 a cada volta no loop
        soma = 0

        # percorre a string
        for i in range(len(string)):
            # soma o digito atual em soma 
            soma += int(string[i])
        # adiciona a soma em lista somados
        listaSomados.append(soma)



    # define menor como o primeiro indice da lista
    menor = listaSomados[0] 

    # percorre a lista com os numeros somados
    for i in range(1, len(listaSomados)):
        # se o indice atual for menor que menor, define menor como o indice atual
        if listaSomados[i] < menor:
            menor = listaSomados[i]

    
    # retorna menor
    return menor


nums = [10,12,13,14]
print(minElement(nums))
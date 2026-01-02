def smallestIndex(nums):


    # lista com os indices que cumprirem os requisitos
    iguais = []

    # percorre nums
    for i in range(len(nums)):
        # transforma o valor atual em string
        stringnums = str(nums[i])
        # inicializa a soma dos digitos
        somaDigitos = 0

        # percorre os digitos da string
        for j in range(len(stringnums)):
            # adiciona o digito atual na soma 
            somaDigitos += int(stringnums[j])
        # se a soma final for igual a i, adiciona na lista
        if somaDigitos == i:
            iguais.append(i)
    
    # se a lista de iguais estiver vazia, retorna -1 imediatamente
    if len(iguais) < 1:
        return -1
    # caso tenha algum valor, encontra o menor valor e retorna ele
    else:
        menor = iguais[0]
        for i in range(len(iguais)):
            if iguais[i] <= menor:
                menor = menor
        return menor

        






nums = [1,10,11]
print(smallestIndex(nums))
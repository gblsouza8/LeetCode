def maxFrequencyElements(nums):

    # variavel que irá contar o maximo de vezes que um digito se repete
    contador = 0
    # variavel que será retornada
    saida = 0
    # lista com os numeros já analisados
    lista = []


    # encontra o máximo de vezes que um digito se repete
    for i in range(len(nums)):
        x = 0
        for j in range(len(nums)):
            if nums[i] == nums[j]: x += 1
        
        if x >= contador:
            contador = x
    

    # incrementa saida para cada numero que se repete a maxima quantidade de vezes
    for i in range(len(nums)):
        if nums[i] not in lista:
            x = 0
            for j in range(len(nums)):
                if nums[i] == nums[j]: x += 1
            if x == contador: 
                lista.append(nums[i])
                saida += contador
    
    return saida







nums = [1,2,2,3,1,4]
print(maxFrequencyElements(nums))
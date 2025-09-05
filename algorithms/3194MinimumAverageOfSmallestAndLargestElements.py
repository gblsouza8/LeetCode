def minimumAverage(nums):

    # lista que irá conter as medias
    averages = []

    # enquanto tiver algo em nums
    while len(nums) > 0:
        # define menor e maior como o indice 0 para percorrer a lista procurando
        menor = nums[0]
        maior = nums[0]
        # define a variavel removerindice1 como 0
        removerIndice1 = 0

        # percorre a lista procurando o menor valor
        for i in range(len(nums)):
            if nums[i] < menor:
                menor = nums[i]
                removerIndice1 = i

        # define a variavel removerindice2 como 0
        removerIndice2 = 0
        # percorre a lista procurnado o maior valor
        for j in range(len(nums)):
            if nums[j] > maior:
                maior = nums[j]
                removerIndice2 = j


        # adiciona a media entre os 2 na lista averages (dividindo por 2.0 porque por 2 tava dando erro por algum motivo)
        averages.append(float((maior + menor) / 2.0))


        # se removerindice1 for maior que indice2, entao o indice2 nao será alterado e poderá ser removido normalmente
        if removerIndice1 > removerIndice2:
            del nums[removerIndice1]
            del nums[removerIndice2]
        # senao, subtrai 1 para poder remover 
        else:
            del nums[removerIndice1]
            del nums[removerIndice2-1]

    
    # encontra o menor valor em average
    x = float(averages[0])
    for i in range(len(averages)):
        if averages[i] < x:
            x = float(averages[i])
    
    # retorna x
    return x
        


    
            
nums = [7,8,3,4,15,13,4,1]
print(minimumAverage(nums))
def numIdenticalPairs(nums):
    # Inicializa o contador de pares
    pares = 0


    # Para cada indice do nums
    for i in range(len(nums)):
        # Irá verificar os indices que vem após o indice i atual
        for j in range(i+1, len(nums)):
            # Se achar outro com o mesmo valor que o indice i, irá incrementar o contador de pares
            if nums[i] == nums[j]:
                pares += 1


    # Retorna o valor final após percorrer o laço todo
    return pares




nums = [1,1,1,1]
print(numIdenticalPairs(nums))
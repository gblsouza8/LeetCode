def transformArray(nums):
    # Inicializa a nova lista que irá armazenar os novos valores
    lista = []

    # Percorre a lista
    for i in range(len(nums)):
        # Se o indice atual for divisivel por 2, adiciona 0
        if nums[i] % 2 == 0:
            lista.append(0)
        # Se não for divisivel por 2, adiciona 1
        else:
            lista.append(1)
    
    # Retorna a lista em ordem crescente
    return sorted(lista)

nums = [4,3,2,1]
print(transformArray(nums))
def sumOfUnique(nums):

    # lista que irá salvar os digitos unicos
    unicos = []
    # variavel que será retornada
    soma = 0

    # percorre os numeros
    for i in range(len(nums)):
        # flag que irá mudar caso encontre um número igual na lista
        flag = False
        # percorre números
        for j in range(len(nums)):
            # se i for igual a j (é o mesmo indice), ignora
            if i == j:
                pass
            # se for diferente
            else:
                # verifica se o indice j é igual ao indice i
                if nums[i] == nums[j]:
                    # caso seja igual, muda a flag para True (encontrou outro numero igual)
                    flag = True
        # se flag sair do for j sendo False, adiciona o numero na lista de unicos
        if flag == False:
            unicos.append(nums[i])
    
    # soma todos os numeros na lista de unicos
    for i in range(len(unicos)):
        soma += unicos[i]
                    
    # retorna soma
    return soma




nums = [1,2,3,2]
print(sumOfUnique(nums))
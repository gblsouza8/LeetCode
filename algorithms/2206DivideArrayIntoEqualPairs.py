def divideArray(nums):


    # lista com os caracteres para evitar contar o mesmo caractere duas vezes
    caracteres = []

    # lista com a quantidade de vezes que os caracteres aparecem
    contagem = []


    # se nums tiver uma quantidade impar de caracteres, já retorna False imediatamente
    if len(nums) % 2 != 0:
        return False


    # percorre nums
    for i in range(len(nums)):

        # se o caractere atual já tiver sido analisado, ignora
        if nums[i] in caracteres:
            pass
        #senão
        else:
            # inicia o contador
            contador = 0

            # percorre nums contando as vezes que o caractere aparece
            for j in range(len(nums)):
                if nums[j] == nums[i]:
                    contador += 1

            # adiciona o contador na lista de quantidade
            contagem.append(contador)

            # adiciona o caractere na lista de caracteres verificados
            caracteres.append(nums[i])
    

    # percorre a lista de quantidade, caso encontre uma quantidade impar retorna False imediatamente.
    for i in range(len(contagem)):
        if contagem[i] % 2 != 0:
            return False
        
    
    # caso chegue até aqui, retorna True
    return True




nums = [1,2,3,4]
print(divideArray(nums))
def decompressRLEList(nums):
    # variavel para o laço while
    i = 0
    # lista que irá ser retornada
    saida = []

    # enquanto i for menor que tamanho de nums - 1
    while i <= len(nums) - 1:
        # frequencia será o indice atual de nums
        freq = nums[i]
        # valro será o indice após o indice atual
        val = nums[i+1]
        # adiciona val na lista saida freq vezes
        for j in range(freq):
            saida.append(val)
        # incrementa i em 2 para garantir que será sempre feito em par
        i = i + 2
    
    # retona saida
    return saida





nums = [65,44,72,15]
print(decompressRLEList(nums))
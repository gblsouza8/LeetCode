def sumIndicesWithKSetBits(nums, k):



    # variavel que irá ser retornada após a soma
    soma = 0

    # converte o indice atual para uma string com o valor binário dele
    for i in range(len(nums)):
        # string vazia para resetar a cada volta no loop
        string = ""
        # x recebe o valor do indice atual
        x = i
        # converte para binario 
        while int(x) > 0:
            string += str(int(x%2))
            x = x / 2


        # inicializa um contador de bits
        contadorK = 0
        # soma todos os digitos da string (versão binária do indice atual)
        for j in range(len(string)):
            contadorK += int(string[j])

        # se os digitos tiverem a exata mesma quantidade que k, irá somar o item que está no indice atual à soma
        if contadorK == k:
            soma += nums[i]


    # retorna soma 
    return soma 









nums = [5,10,1,5,2]
k = 1
print(sumIndicesWithKSetBits(nums, k))
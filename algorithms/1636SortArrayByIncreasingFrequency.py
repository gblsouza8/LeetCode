def frequencySort(nums):

    # lista que será montada e colocada na ordem
    lista = []
    while True:
        # define valores para comparação nos laços
        menor = nums[0]
        quantidade = nums.count(nums[0])

        # percorre os numeros em nums
        for i in range(len(nums)):

            # verifica se o numero atual aparece menos vezes ou igualmente ao numero que está armazenado nas variaveis e se o indice atual é maior que o indice que está nas variaveis
            if nums.count(nums[i]) <= quantidade and nums[i] > menor:
                # se for, muda os valores
                quantidade = nums.count(nums[i])
                menor = nums[i]
            # verifica se a quantidade de vezes é simplesmente menor que a armazenada atualmente
            if nums.count(nums[i]) < quantidade:
                # se for, muda os valores
                quantidade = nums.count(nums[i])
                menor = nums[i]
        
        # percorre o laço a quantidade de vezes que o valor encontrado aparece
        for i in range(quantidade):
            # adiciona o menor valor na lista que será retornada
            lista.append(menor)
            # remove o valor de nums
            nums.remove(menor)

        # verifica se nums ainda tem um tamanho maior que 1 (digitos sobrando)
        if len(nums) < 1:
            # se não tiver, sai do laço while
            break

    # retorna a lista ordenada
    return lista












nums = [1,1,2,2,2,3]
print(frequencySort(nums))

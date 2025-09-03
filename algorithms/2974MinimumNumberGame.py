def numberGame(nums):

    # listas 
    alice = []
    bob = []
    arr = []

    # variavel indice (para remover o menor valor)
    indice = 0
    # variavel com a metade do tamanho original para fazer a inserção em arr
    tamanho = int(len(nums)/2)



    # enquanto nums tiver algum indice
    while len(nums) > 0:


        # encontra o menor valor 
        menor = nums[0]
        for i in range(len(nums)):
            if nums[i] < menor:
                menor = nums[i]
                indice = i
        # adiciona na lista alice e remove do nums
        alice.append(nums.pop(indice))

        # reinicia a variavel indice para 0
        indice = 0

        # encontra o novo menor valor
        menor = nums[0]
        for i in range(len(nums)):
            if nums[i] < menor:
                menor = nums[i]
                indice = i
        # adiciona o menor valor em bob e remove de nums
        bob.append(nums.pop(indice))

        # reinicia a variavel indice para 0
        indice = 0




    # monta a saida em ordem, primeiro o removido pelo bob e depois o removido por alice
    for i in range(tamanho):
        arr.append(bob[i])
        arr.append(alice[i])

    # retorna a array final
    return arr



        

nums = [2,5,3,8]
print(numberGame(nums))
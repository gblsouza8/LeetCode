def countPairs(nums, target):
    # inicializa a variavel com o contador
    contador = 0

    # percorre a lista
    for i in range(len(nums)):
        # percorre a lista já dentro do laço for, para comparar o indice i com os indices restantes da lista
        for j in range(len(nums)):
            # se  i for menor que j
            if i < j:
                # soma ambos e caso seja menor que target, incrementa o contador
                if nums[i] + nums[j] < target:
                    contador += 1

    # retorna o contador
    return contador


nums = [-1,1,2,3,1]
target = 2
print(countPairs(nums, target))
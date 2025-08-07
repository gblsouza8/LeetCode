def leftRightDifference(nums):
    # Inicializa as listas
    saida = []
    direita = []
    esquerda = []


    # Percorre a lista
    for i in range(len(nums)):
        # Inicia a variavel soma que irá salvar na lista
        soma = 0
        # Soma todos os valores que vem após o indice atual
        for j in range(i+1, len(nums)):
            soma += nums[j]
        # Adiciona a lista
        direita.append(soma)


    for i in range(len(nums)):
        soma = 0
        # Soma todos os valores que vem antes do indice atual
        for j in range(0, i):
            soma += nums[j]
        # Adiciona a lista
        esquerda.append(soma)


    # Monta a lista com o resultado, subtraindo indice por indice das duas listas
    for i in range(len(nums)):
        saida.append(abs(direita[i] - esquerda[i]))

    return saida





nums = [10,4,8,3]
print(leftRightDifference(nums))

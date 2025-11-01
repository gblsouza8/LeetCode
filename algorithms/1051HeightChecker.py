def heightChecker(heights):

    # contador
    contador = 0

    # gera uma nova lista que será a versão em ordem crescente de heights
    ordemCrescente = sorted(heights)

    # percorre heights
    for i in range(len(heights)):
        # para cada valor diferente da ordemCrescente, incrementa o contador
        if heights[i] != ordemCrescente[i]:
            contador += 1

    # retorna o contador
    return contador





heights = [1,1,4,2,1,3]
print(heightChecker(heights))
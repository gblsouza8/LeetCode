def getSneakyNumbers(nums):
    # Inicializa as listas que irão receber os numeros encontrados na lista nums
    numerosEncontrados = []
    numerosRepetidos = []

    # Percorre a lista nums
    for i in range(len(nums)):
        # Adiciona todos os primeiros encontros na lista numerosEncontrados
        if nums[i] not in numerosEncontrados:
            numerosEncontrados.append(nums[i])
        # Se o numero já estiver na lista de numerosEncontrados, adiciona na lista de numerosRepetidos
        else:
            numerosRepetidos.append(nums[i])

    # Retorna a lista, usando o sorted para colocar em ordem crescente
    return sorted(numerosRepetidos)

nums = [7,1,5,4,3,4,6,0,9,5,8,2]
print(getSneakyNumbers(nums))
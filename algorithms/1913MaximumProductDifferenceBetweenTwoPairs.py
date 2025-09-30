def maxProductDifference(nums):

    # variaveis para identificar os dois maiores valores da lista
    maior1 = 0
    maior2 = 0

    # variaveis para identificar os dois menores valores da lista
    menor1 = 10000000
    menor2 = 10000000


    # percorre os numeros em nums
    for num in nums:
        

        # se o numero atual for maior que o maior1, maior2 (segundo maior) assume o valor de maior1 e maior1 vira o numero
        if num > maior1:
            maior2 = maior1
            maior1 = num
            
        # se o numero atual for apenas maior que o segundo maior, maior2 vira o numero
        elif num > maior2:
            maior2 = num
        


        # se o numero atual for menor que o menor numero, menor2 vira menor1 e menor1 vira o numero
        if num < menor1:
            menor2 = menor1
            menor1 = num
        # se o numero atual for apenas menor que o segundo menor, menor2 vira o numero
        elif num < menor2:
            menor2 = num

            
    # retorna a diferença entre o maior e o menor produto
    return (maior1 * maior2) - (menor1 * menor2)





nums = [8,3,5,7]
print(maxProductDifference(nums))
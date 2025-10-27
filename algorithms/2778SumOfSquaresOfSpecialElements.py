def sumOfSquares(nums):

    # tamanho de nums
    n = len(nums)
    # variavel soma 
    soma = 0

    # percorre nums
    for i in range(len(nums)+1):
        # soma +1 ao i para não tentar a divisão por 0
        x = i+1
        # se n for divisivel por x, incrementa soma com o quadrado do indice i
        if n % x == 0:
            soma = soma + nums[i] * nums[i]

    # retorna soma
    return soma




nums = [1,2,3,4]
print(sumOfSquares(nums))
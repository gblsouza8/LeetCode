def maxProduct(nums):

    # varivel q irá armazenar o maximo valor
    max = 0

    # percorre a lista 
    for i in range(len(nums)):
        
        # percorre a lista a partir do i atual
        for j in range(i+1, len(nums)):

            # verifica se o produto dos 2 indices atuais é maior que o maximo até o momento, e se for, substitui por ele
            valorAtual = (nums[i]-1) * (nums[j]-1)
            if valorAtual > max:
                max = valorAtual
    # retorna o maximo valor
    return max





nums = [3,4,5,2]
print(maxProduct(nums))
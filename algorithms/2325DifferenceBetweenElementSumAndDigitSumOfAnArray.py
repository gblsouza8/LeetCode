def differenceOfSum(nums):

    # variaveis que irão armazenar as somas
    somaElementos = 0
    somaDigitos = 0
    # string para pegar digito por digito
    string = ""

    # soma os elementos e forma a string digito por digito
    for i in range(len(nums)):
        somaElementos += nums[i]
        string += str(nums[i])


    # soma os digitos percorrendo a string formada
    for i in range(len(string)):
        somaDigitos += int(string[i])

    # retorna a diferença entre a soma dos elementos e a soma dos digitos
    return somaElementos - somaDigitos



nums = [1,15,6,3]
print(differenceOfSum(nums))


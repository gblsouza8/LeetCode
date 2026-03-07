def findNumbers(nums):


    # variavel para incrementar a cada numero com digitos pares
    contador = 0

    # percorre os digitos
    for i in range(len(nums)):

        # transforma o indice atual em string para poder contar os digitos
        string_numero = str(nums[i])
        # se a quantidade de digitos for par, incrementa o contador
        if len(string_numero) % 2 == 0:
            contador += 1


            
    # retorna o contador
    return contador





nums = [12,345,2,6,7896]
print(findNumbers(nums))
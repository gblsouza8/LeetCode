def isArraySpecial(nums):
    # flag que será retornada caso a array não seja reprovada em nenhum teste
    flag = True


    # retorna true imediatamente caso o tamanho da array seja 1
    if len(nums) == 1:
        return True
    

    # percorre a array
    for i in range(len(nums)):

        # verifica se não é o ultimo indice para evitar o erro out of range
        if i < len(nums)-1:


            # se o indice atual for par, verifica se o sucessor também é, caso seja, retorna False
            if nums[i] % 2 == 0:
                if nums[i+1] % 2 == 0:
                    return False
                else:
                    pass


            # se o indice atual for impar, verifica se o sucessor também é, caso seja, retorna False
            else:
                if nums[i] % 2 != 0:
                    if nums[i+1] % 2 != 0:
                        return False
                    else:
                        pass


    # retorna flag caso passe por todo o laço
    return flag




nums = [4,3,1,6]
print(isArraySpecial(nums))
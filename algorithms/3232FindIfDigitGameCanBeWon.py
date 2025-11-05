def canAliceWin(nums):

    # variaveis que irá somar os números com um e dois digitos
    alice = 0
    bob = 0
    # string que para contar a quantidade de digitos em cada numero
    string = ""

    # percorre a lista
    for i in range(len(nums)):
        # transforma o indice atual em uma string
        string += str(nums[i])
        # se a quantidade de digitos for 1, soma em alice
        if len(string) == 1:
            alice += nums[i]
        # se nao for 1 (é 2), soma em bob
        else:
            bob += nums[i]

        # limpa a string para o próximo numero
        string = ""

    # se ao sair do laço, alice (1 digito) for maior que bob ou bob (2 digitos) for maior que alice
    if alice > bob or bob > alice:
        # retorn true
        return True
    # se nenhum for maior que o outro
    else:
        # retorna false
        return False






nums = [5,5,5,25]
print(canAliceWin(nums))
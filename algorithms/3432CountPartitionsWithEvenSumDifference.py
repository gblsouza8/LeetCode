def countPartitions(nums):


    # variaveis que serão utilizadas
    soma_depois = 0
    soma_ate = 0
    contador_pares = 0

    # percorre nums
    for i in range(len(nums)-1):
        # soma até o i atual
        soma_ate += nums[i]

        # soma todos os valores que vem depois do i
        for j in range(i+1, len(nums)):
            soma_depois += nums[j]
 
        # se a soma até i - a soma de tudo que vem depois for par, incrementa o contador
        if abs(soma_ate - soma_depois) % 2 == 0:
            contador_pares += 1

        # reinicia a variavel de soma do que vem depois de i
        soma_depois = 0

    # retorna o contador de numeros pares
    return contador_pares


nums = [2,4,6,8]
print(countPartitions(nums))
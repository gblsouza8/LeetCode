def minimumOperations(nums):
    contador = 0

    # Percorre a lista 
    for i in range(len(nums)):
        # Define a variável x como o indice atual da lista
        x = nums[i]
        # Se x + 1 ou x - 1 for divisivel por 3, incrementa o contador em 1
        if (x+1) % 3 == 0 or (x-1) % 3 == 0:
            contador += 1
    # Retorna o contador
    return contador


nums = [3,6,9]
print(minimumOperations(nums))
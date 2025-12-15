def separateDigits(nums):

    # array que será construida e retornada
    novaArray = []

    # percorre nums
    for i in range(len(nums)):
        # transforma nums atual em uma string
        string = str(nums[i])
        # percorre a string
        for j in range(len(string)):
            # adiciona o digito atual da string em novaArray
            novaArray.append(int(string[j]))
    # retorna a novaArray
    return novaArray
        



nums = [13,25,83,77]
print(separateDigits(nums))
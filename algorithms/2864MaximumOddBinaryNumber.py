def maximumOddBinaryNumber(s):

    # contadores de 1 e 0
    contador1 = 0
    contador0 = 0
    # string vazia que será moldada e retornada
    string = ""

    # percorre a string contando os 1 e os 0
    for i in range(len(s)):
        if s[i] == "1":
            contador1 += 1
        elif s[i] == "0":
            contador0 += 1



    # adiciona 1 a string usando como base o valor do contador - 1 (ultimo 1)
    for i in range(contador1-1):
        string += "1"


    # adiciona os 0 após adicionar os 1
    for i in range(contador0):
        string += "0"

    # adiciona o 1 restante (ultimo 1)
    string += "1"


    # retorna a string
    return string
        





s = "010"
print(maximumOddBinaryNumber(s))
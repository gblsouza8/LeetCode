def isStrictlyPalindromic(n):


    # variavel para converter o numero em bases
    x = n
    flag = True

    # da base 2 até a base n-2
    for i in range(2, n-1):
        # atribui o valor de n para x
        x = n
        # reinicia a string a cada volta no laço
        string = ""
        # enquanto x for maior que 0
        while x > 0:
            # pega o resto
            resto = int(x%i)
            # divide x por i
            x = int(x/i)
            # adiciona o resto na string
            string += str(resto)
        # ao sair do while, compara a string com sua versão invertida
        stringReverso = string[:-1]
        # caso sejam diferentes, retorna false
        if stringReverso != string:
            return False
    # caso saia do laço for, retorna True
    return flag





n = 4
print(isStrictlyPalindromic(n))
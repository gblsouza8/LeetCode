def removeTrailingZeros(num):

    # laço while que apenas sairá quando retornar algo
    while True:
        # se o último caractere de num for 0, reescreve a string até ele
        if num[-1] == "0":
            num = num[:-1]
        #se não for 0, retorna a string
        else:
            return num





num = "31514216007864075756059111751787923413952537015859352242147727420"
print(removeTrailingZeros(num))
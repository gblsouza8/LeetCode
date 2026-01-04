def hasSameDigits(s):

    # repete enquanto a string tiver mais de dois digitos
    while len(s) > 2:

        # variavel temporaria para realizar a operação
        s2 = ""
        # percorre a string(-1 para evitar erro de out of range)
        for i in range(len(s)-1):
            # realiza a operação
            operacao = int(int(s[i]) + int(s[i+1])) % 10
            # adiciona a operação na string temporaria
            s2 += str(operacao)
        # atribui o valor da string temporaria na string
        s = s2

    # quando sair do laço while (s tem 2 digitos)
    # verifica se o primeiro digito é diferente do segundo
    if s[0] != s[1]:
        # se for, retorna False
        return False
    #senão, retorna True
    else:
        return True


s = "3902"
print(hasSameDigits(s))
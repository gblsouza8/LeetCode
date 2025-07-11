def RomanToInteger(s):
    # Define a variável x onde irá alterar conforme o resultado
    x = 0
    tam = len(s)
    # Caso o tamanho seja 1, ou seja, tenha apenas um caractere, irá simplesmente exibir o resultado
    if tam == 1:
        letras = ("I", "V", "X", "L", "C", "D", "M")
        valores = (1, 5, 10, 50, 100, 500, 1000)
        for i in range(len(letras)):
            if s == letras[i]:
                x = valores[i]
                return x
    # Se não, irá montar o valor seguindo as verificações
    else:
        for i in range(tam):
            # Valores que alteram o valor do próximo número
            if s[i] == "I":
                # Verifica se é o último digito
                if i < tam - 1:
                    if s[i+1] == "V":
                        x = x + 4
                    elif s[i+1] == "X":
                        x = x + 9
                    else:
                        x = x + 1
                # Caso seja o último digito e não tenha nada a seguir, apenas soma +1
                else:
                    x = x + 1

            elif s[i] == "X":
                # Verifica se é o primeiro digito para que não haja o erro de não somar o valor inicial
                if i == 0:
                    # Verifica o que vem após o índice para realizar as possíveis subtrações
                    if s[i+1] == "L":
                        x = x + 40
                    elif s[i+1] == "C":
                        x = x + 90
                    else:
                        x = x + 10
                else:
                    # Caso o índice anterior seja I, já realizou a subtração então não faz nada
                    if s[i-1] == "I":
                        pass
                    else:
                        # Caso não seja, realiza a verificação se é o último digito e caso não seja, realiza a verificação do próximo
                        if i < tam - 1:
                            if s[i+1] == "L":
                                x = x + 40
                            elif s[i+1] == "C":
                                x = x + 90
                            else:
                                x = x + 10
                        # Se for o último digito, soma +10 ao x
                        else:
                            x = x + 10


            elif s[i] == "C":
                if i == 0:
                    if s[i+1] == "D":
                        x = x + 400
                    elif s[i+1] == "M":
                        x = x + 900
                    else:
                        x = x + 100
                else:
                    if s[i-1] == "X":
                        pass
                    else:
                        if i < tam - 1:
                            if s[i+1] == "D":
                                x = x + 400
                            elif s[i+1] == "M":
                                x = x + 900
                            else:
                                x = x + 100
                        else:
                            x = x + 100


            # Mil
            elif s[i] == "M":
                if i == 0:
                    x = x + 1000
                else:
                    if s[i-1] == "C":
                        pass
                    else:
                        x = x + 1000

            # Valores equivalentes a "5" que não alteram o valor do próximo número
            elif s[i] == "V":
                if i == 0:
                    x = x + 5
                else:
                    if s[i-1] == "I":
                        pass
                    else:
                        x = x + 5

            elif s[i] == "L":
                if i == 0:
                    x = x + 50
                else:
                    if s[i-1] == "X":
                        pass
                    else:
                        x = x + 50

            elif s[i] == "D":
                if i == 0:
                    x = x + 500
                else:
                    if s[i-1] == "C":
                        pass
                    else:
                        x = x + 500
        
        return x

print(RomanToInteger("C"))
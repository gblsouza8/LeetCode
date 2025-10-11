def replaceDigits(s):

    # listas com digitos e letras que aparecerão
    digitos = ["0", "1", "2", "3", "4", "5", "6", "7", "8", "9"]
    alfabeto = ["a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m", "n", "o", "p", "q", "r", "s", "t", "u", "v", "w", "x", "y", "z"]
    
    # percorre a string
    for i in range(len(s)):

        # se o caractere atual estiver em digitos (for um digito)
        if s[i] in digitos:
            # encontra a letra anterior a ele 
            caractereAnterior = s[i-1]
            # converte o caractere atual em inteiro e armazena na variavel digito
            digito = int(s[i])

            # percorre alfabeto 
            for j in range(len(alfabeto)):
                # encontra o caractereAnterior em alfabeto
                if alfabeto[j] == caractereAnterior:
                    # define que o novoCaractere (que substituirá o digito) será o indice que é a soma do caractere anterior + digito
                    novoCaractere = alfabeto[j+digito]
                    break
            
            # substitui a primeira ocorrencia do digito pelo novo caractere
            s = s.replace(s[i], novoCaractere, 1)

    # retorna s
    return s



        








s = "a1c1e1"
print(replaceDigits(s))
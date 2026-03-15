def halvesAreAlike(s):


    # variavel que conta as vogais em cada metade
    contadorVogais1 = 0
    contadorVogais2 = 0

    # lista com as vogais
    vogais = ["a", "e", "i", "o", "u"]

    # tamanho da metade da string
    metade = int(len(s)/2)


    # percorre a primeira metade da string
    for i in range(int(len(s)/2)):
        # se o caractere for uma vogal, incrementa o contador
        if s[i].lower() in vogais:
            contadorVogais1 += 1

    # percorre a segunda metade da lista
    for i in range(metade, (len(s))):
        # se o caractere for uma vogal, incrementa o  contador
        if s[i].lower() in vogais:
            contadorVogais2 += 1

    # retorna o resultado da verificação de ambas as variaveis serem iguais
    return contadorVogais1 == contadorVogais2

s = "textbook"
print(halvesAreAlike(s))
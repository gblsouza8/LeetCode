def ScoreOfString(s):

    # Tamanho da string
    tam = len(s)
    # Listas com as letras do alfabeto
    letras = ["a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m", "n", "o", "p", "q", "r", "s", "t", "u", "v", "w", "x", "y", "z"]
    # Lista com os valores ASCII de cada letra
    valores = [97, 98, 99, 100, 101, 102, 103, 104, 105, 106, 107, 108, 109, 110, 111, 112, 113, 114, 115, 116, 117, 118, 119, 120, 121, 122]
    # Lista que irá armazenar os valores após comparar cada letra da string
    listaValores = []
    # Lista com os valores após a subtração
    listaValoresSub = []
    # Variável que irá armazenar o score
    score = 0

    # Percorre a string comparando o caractere atual com os caracteres da lista de letras e adiciona o valor na lista caso encontre
    for i in range(tam):

        for j in range(len(letras)):
            if s[i] == letras[j]:
                listaValores.append(valores[j])
            else:
                pass
    
    # Percorre a lista dos valores encontrados na string realizando a subtração, adicionando na lista transformando os numeros negativos em positivos
    for i in range(len(listaValores) - 1):
        listaValoresSub.append(abs(listaValores[i] - listaValores[i+1]))

    # Soma cada número da lista subtraida para a variável score
    for i in range(len(listaValoresSub)):
        score += listaValoresSub[i]


    # Retorna o score
    return score



s = "hello"
print(ScoreOfString(s))

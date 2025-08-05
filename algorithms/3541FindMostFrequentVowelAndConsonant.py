def maxFreqSum(s):
    # Encontrar a maior frequencia de vogal

    # Inicializa a lista com as vogais
    vogais = ["a", "e", "i", "o", "u"]

    # Define que x inicialmente tem o valor da quantidade de vezes que o 
    # primeiro indice de vogais se repete  
    x = s.count(vogais[0])

    # Percorre a lista de vogais
    for i in range(1, len(vogais)):
        # Compara a quantidade de vezes que o indice atual aparece na string com o valor atual de x
        if s.count(vogais[i]) > x:
            # Se for maior, substitui
            x = s.count(vogais[i])

    # Após parar de percorrer a lista, define que o contador de vogais terá o valor final de x
    contador_vogais = x

    # Encontrar a maior frequencia de consoante

    # Lista de consoantes
    consoantes = ["b", "c", "d", "f", "g", "h", "j", "k", "l", "m", "n", "p", "q", "r", "s", "t", "v", "w", "x", "y", "z"]
    # Define o valor de x como o primeiro indice de consoantes
    x = s.count(consoantes[0])

    # Percorre a lista de consoantes
    for i in range(1, len(consoantes)):
        # Compara a quantidade de vezes que o indice atual aparece na string com o valor atual de x
        if s.count(consoantes[i]) > x:
            # Se for maior, substitui
            x = s.count(consoantes[i])

    # Após parar de percorrer a lista, define que o contador de vogais terá o valor final de x
    contador_consoantes = x



    # Retorna a soma de ambos
    return contador_vogais + contador_consoantes

s = "successes"
print (maxFreqSum(s))
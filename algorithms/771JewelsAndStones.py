def numJewelsInStones(jewels, stones):
    # Inicializa a lista que irá armazenar a lista de jewels encontradas na string
    listaJewels = []
    # Inicializa o contador a ser incrementado a cada jewel em stones
    contador = 0

    # Adiciona cada caractere da string jewels na lista
    for i in range(len(jewels)):
        listaJewels.append(jewels[i])

    # Verifica cada caractere de stones para saber se está na lista de jewels
    for i in range(len(stones)):
        if stones[i] in listaJewels:
            # Se estiver, incrementa o contador
            contador +=1

    # Retorna o contador
    return contador







jewels = "aA"
stones = "aAAbbbb"
print (numJewelsInStones(jewels, stones))
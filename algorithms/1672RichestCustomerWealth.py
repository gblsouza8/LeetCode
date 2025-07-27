def maximumWealth(accounts):
    # Define as variáveis que serão usadas para comparação
    maior = 0
    x = 0

    # Define que a primeira lista (0) será o maior valor 
    for i in range(len(accounts[0])):
        maior += accounts[0][i]

    # Percorre as outras listas a partir da segunda lista (1)
    for i in range(1,(len(accounts))):
        # Soma os indices da lista atual na variável x
        for j in range(0, len(accounts[i])):
            x += accounts[i][j]
        # Se x for maior que a soma atual na variavel maior, maior virará x e irá zerar x para somar a próxima lista
        if x > maior:
            maior = x
            x = 0
        # Senão, irá apenas zerar x para somar a próxima lista
        else: 
            x = 0

    # Retorna o valor final 
    return maior


accounts = [[1,5],[7,3],[3,5]]
print(maximumWealth(accounts))


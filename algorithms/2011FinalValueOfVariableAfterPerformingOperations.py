def finalValueAfterOperations(operations):
    # Define a variável que irá receber as operações de decremento ou incremento
    x = 0
    # Percorre a lista de operações
    for i in range(len(operations)):
        # Se o indice atual for --X ou X-- irá decrementar x em 1
        if operations[i] == "--X" or operations[i] == "X--":
            x -= 1
        # Se o inice atual for ++X ou X++ irá incrementar x em 1
        elif operations[i] == "++X" or operations[i] == "X++":
            x += 1

    # Retorna x após percorrer toda a lista
    return x





operations = ["--X","X++","X++"]
print(finalValueAfterOperations(operations))
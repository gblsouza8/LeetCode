def minOperations(boxes):

    # lista que será retornada
    saida = []
    # percorre as boxes
    for i in range(len(boxes)):

        # reinicia o contador a cada volta no laço
        contador = 0

        # percorre as boxes para comparar com o i atual
        for j in range(len(boxes)):
            # caso sejam o mesmo indice, ignora
            if i == j:
                pass
            # caso nao sejam o mesmo indice
            else:
                # se encontrar mais uma box com algo
                if boxes[j] == '1':
                    # incrementa o contador na quantidade de indices caminhados de i até j
                    contador += abs(i-j)
        # adiciona o contador na lista de saida
        saida.append(contador)
    # retorna a lista                
    return saida






boxes = "110"
print(minOperations(boxes))
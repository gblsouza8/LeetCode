def flipAndInvertImage(image):


    # lista para inverter as colunas
    image1 = []
    # lista para trocar os numeros 1 e 0
    image2 = []
    # lista temporaria para auxiliar na troca dos numeros
    listaTemp = []

    # invertendo os valores
    for i in range(len(image)):
        image1.append(list(reversed(image[i])))

    
    # percorre image1
    for j in range(len(image1)):
        # reseta listaTemp a cada volta no laço for
        listaTemp = []
        # verifica cada indice da lista atual
        for k in range(len(image1[j])):
            # se for 1, adiciona 0 na listaTemp
            if image1[j][k] == 1:
                listaTemp.append(0)
            # se nao for 1 (é 0), adiciona 1
            else:
                listaTemp.append(1)
        # adiciona listaTemp em image2
        image2.append(listaTemp)
    
    # retorna image2
    return image2




image = [[1,1,0],[1,0,1],[0,0,0]]
print(flipAndInvertImage(image))
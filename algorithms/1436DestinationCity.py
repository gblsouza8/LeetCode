def destCity(paths):


    # cidades de ida
    cidades1 = []

    # cidades de destino
    cidades2 = []


    # monta as listas
    for i in range(len(paths)):
        cidades1.append(paths[i][0])
        cidades2.append(paths[i][1])


    # encontra qual cidade de destino que não aparece nenhuma vez em cidades de ida
    for i in range(len(cidades2)):
        if cidades2[i] not in cidades1:
            return cidades2[i]





paths = [["London","New York"],["New York","Lima"],["Lima","Sao Paulo"]]
print(destCity(paths))
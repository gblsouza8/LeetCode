def findCenter(edges):
    
    # declarando a variavel flag para verificar se o indice esta em todas as outras listas
    flag = True
    # percorre apenas os 2 primeiros indices de edges
    for i in range(2):
        # reseta flag para true
        flag = True
        # percorre todos os indices de edges
        for j in range(len(edges)):
            # se o indice atual não aparecer em algum momento nas outras listas
            if edges[0][i] not in edges[j]:
                # define a flag como False
                flag = False
                # para de percorrer esse indice
                break
        # se flag sair do segundo laço como true, retorna o indice que apareceu em todos os edges
        if flag == True:
            return edges[0][i]





edges = [[1,2],[5,1],[1,3],[1,4]]
print(findCenter(edges))
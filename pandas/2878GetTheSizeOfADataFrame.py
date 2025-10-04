import pandas as pd

def getDataframeSize(players: pd.DataFrame) -> List[int]:
    # inicializa uma lista
    lista = []

    # adiciona na lista a quantidade de linhas
    lista.append(players.shape[0])
    # adiciona na lista a quantidade de colunas
    lista.append(players.shape[1])

    # retorna a lista
    return lista
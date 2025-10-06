import pandas as pd

def createDataframe(student_data: List[List[int]]) -> pd.DataFrame:

    # define os nomes das colunas
    colunas = ['student_id', 'age']

    # cria o dataframe usando a lista student_data como base
    df = pd.DataFrame(student_data, columns=colunas)

    # retorna o dataframe
    return df
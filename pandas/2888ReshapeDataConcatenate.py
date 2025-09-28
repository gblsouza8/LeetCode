import pandas as pd

def concatenateTables(df1: pd.DataFrame, df2: pd.DataFrame) -> pd.DataFrame:

    # cria um novo dataframe concatenando os dois verticalmente
    resultado = pd.concat([df1, df2])


    # retorna o novo dataframe
    return resultado
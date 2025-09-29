import pandas as pd

def createBonusColumn(employees: pd.DataFrame) -> pd.DataFrame:
    # cria a coluna bonus no dataframe employees utilizando como valores os valores inseridos em salary multiplicado por 2
    employees['bonus'] = employees['salary'] * 2

    # retorna o dataframe
    return employees
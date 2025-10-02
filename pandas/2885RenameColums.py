import pandas as pd

def renameColumns(students: pd.DataFrame) -> pd.DataFrame:

    # dicionário com os nomes que serão trocados
    novosNomes = {
        'id': 'student_id',
        'first': 'first_name',
        'last': 'last_name',
        'age': 'age_in_years'
    }

    # renomeia as colunas
    students.rename(columns=novosNomes, inplace=True)
    # retorna o df
    return students
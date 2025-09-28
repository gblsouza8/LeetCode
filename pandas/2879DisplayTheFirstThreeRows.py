import pandas as pd

def selectFirstRows(employees: pd.DataFrame) -> pd.DataFrame:
    # retorna os três indices no topo do dataframe
    return employees.head(3)
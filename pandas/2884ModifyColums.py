import pandas as pd

def modifySalaryColumn(employees: pd.DataFrame) -> pd.DataFrame:
    # multiplica os itens da coluna salary por 2
    employees['salary'] = employees['salary'] * 2
    return employees
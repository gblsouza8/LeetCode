import pandas as pd

def changeDatatype(students: pd.DataFrame) -> pd.DataFrame:
    # muda a coluna 'grade' do dataframe students para int 
    students['grade'] = students['grade'].astype(int)
    return students
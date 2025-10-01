import pandas as pd

def meltTable(report: pd.DataFrame) -> pd.DataFrame:
    # cria um novo dataframe, derretendo os "quarter_" para valores na coluna quarter e definindo os valores que estavam neles em sales
    novodf = pd.melt(report, id_vars=['product'], value_vars=['quarter_1', 'quarter_2', 'quarter_3', 'quarter_4'], var_name='quarter', value_name = 'sales')

    # retorna o novo dataframe
    return novodf
import pandas as pd

def findHeavyAnimals(animals: pd.DataFrame) -> pd.DataFrame:

    # retorna todos os nomes onde a coluna weight for maior que 100, ordenados em forma decrescente
    return animals[animals['weight'] > 100].sort_values(['weight'],ascending=False)[['name']] 
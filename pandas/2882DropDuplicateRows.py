import pandas as pd

def dropDuplicateEmails(customers: pd.DataFrame) -> pd.DataFrame:
    df_semduplicatas = customers.drop_duplicates(subset=['email'])
    return df_semduplicatas
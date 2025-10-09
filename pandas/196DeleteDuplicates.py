import pandas as pd

def delete_duplicate_emails(person: pd.DataFrame) -> None:

    # ordena o dataframe pelo id, garantindo que a primeira aparição do email será a que ficará
    person.sort_values(by='id', inplace=True)
    
    # deleta todas as duplicatas na coluna e-mail
    person = person.drop_duplicates(subset=['email'], inplace=True)
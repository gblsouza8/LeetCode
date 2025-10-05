def pivotTable(weather: pd.DataFrame) -> pd.DataFrame:

    # Define que os valores da coluna month irão virar linhas, que os valores da coluna city irão virar colunas e que os valores inseridos em temperature irão para as novas colunas (city) 
    weather = weather.pivot(index="month", columns="city", values="temperature")
    return weather
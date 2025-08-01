def kidsWithCandies(candies, extraCandies):
    # Lista que irá salvar os resultados a serem retornados
    lista = []
    
    # Percorre a lista de candies
    for i in range(len(candies)):
        # Define que x será a soma do indice atual com as extraCandies
        x = candies[i]+extraCandies

        # Percorre a lista novamente, agora comparando o x com os outros indices
        for j in range(len(candies)):
            # Se x for menor que o indice atual, y ganhará False e irá terminar o laço
            if x < candies[j]:
                y = False
                break
            # Se não, y irá ganhar True e seguirá o laço normalmente
            else:
                y = True
        # Adiciona o valor de y após sair do laço
        lista.append(y)




    # Retorna a lista com os booleans
    return lista



candies = [2,3,5,1,3]
extraCandies = 3
print(kidsWithCandies(candies, extraCandies))
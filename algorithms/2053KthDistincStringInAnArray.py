def kthDistinct(arr, k):


    # listas que serão usadas para a verificação das palavras
    palavras = []
    palavrasUnicas = []

    # adiciona cada palavra sem repetição na lista palavras
    for i in range(len(arr)):
        if arr[i] not in palavras: 
            palavras.append(arr[i])



    # conta cada vez cada palavra em palavras aparece no arr
    for i in range(len(palavras)):
        # reinicia o contador para 0
        contador = 0

        # percorre a lista arr
        for j in range(len(arr)):
            # compara a palavra atual com cada indice em arr
            if palavras[i] == arr[j]:
                # incrementa o contador sempre que a palavra aparece em arr
                contador += 1
        
        # se o contador for 1 (só aparece uma vez), adiciona a palavra em palavrasUnicas
        if contador == 1:
            palavrasUnicas.append(palavras[i])



    # se k-1 for maior que a lista de palavrasUnicas-1, retorna "" pois não há o indice K a ser retornado
    if k-1 > len(palavrasUnicas)-1:
        return ""
    
    # se nao for maior, retorna o indice pedido
    else:
        return palavrasUnicas[k-1]


arr = ["a","a"]
k = 1
print(kthDistinct(arr, k))
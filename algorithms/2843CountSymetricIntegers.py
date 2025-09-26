def countSymmetricIntegers(low, high):

    # variaveis que serao usadas
    count = 0
    metade1 = []
    metade2 = []
    parada = 0
    soma1 = 0
    soma2 = 0

    # percorre os numeros de low ate high
    for i in range(low, high+1):

        # reinicia as listas com as metades dos numeros 
        metade1 = []
        metade2 = []
        # transforma o numero atual em string para percorrer os digitos
        string = str(i)
        tam = int(len(string))
        # apenas realiza as operações se o numero de digitos for par
        if tam % 2 == 0:

            # pega a primeira metade dos digitos e marca onde parou
            for j in range(int(tam/2)):
                metade1.append(int(string[j]))
                parada = j
            # continua pegando a segunda metade partir de onde parou na primeira metade
            for x in range(parada+1, tam):
                metade2.append(int(string[x]))
            
            
            # reinicia as variaveis de soma
            soma1 = 0
            soma2 = 0

            # soma os digitos da primeira metade
            for k in range(len(metade1)):
                soma1 += metade1[k]
            
            # reinicia k para evitar problemas no laço
            k = 0
            # soma os digitos da segunda metade
            for k in range(len(metade2)):
                soma2 += metade2[k]
            # se ambas as somas forem iguais, incrementa o contador em 1
            if soma1 == soma2:
                count += 1
    # retorna a soma 
    return count




low = 1
high = 100
print(countSymmetricIntegers(low, high))
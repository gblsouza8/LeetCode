def gcdOfOddEvenSums(n):


    # variaveis
    impar = 1
    par = 2
    impares = []
    pares = []
    somaPares = 0
    somaImpares = 0
    restos = []


    # calcula a soma dos impares
    for i in range(n):
        impares.append(impar)
        impar += 2
        somaImpares += impares[i]


    # calcula a soma dos pares
    for i in range(n):
        pares.append(par)
        par += 2
        somaPares += pares[i]


    # definição das variaveis que serão usadas no laço while para calcular o MDC
    i = 1
    # encontra o maior entre as duas somas
    if somaImpares > somaPares:
        maior = somaImpares
        menor = somaPares
    else:
        maior = somaPares
        menor = somaImpares




    while True:
        # divide maior por menor
        x = int(maior / menor)
        # adiciona o resto na lista de restos
        resto = int(maior % menor)
        restos.append(resto)

        # se resto chegar a 0, sai do laço
        if resto < 1:
            break
        # enquanto resto não for 0, o divisor vira o dividendo e o resto vira o divisor
        else:
            maior = menor
            menor = resto


    
    # se a lista de restos tiver apenas um numero, o ultimo divisor não-nulo foi 1
    if len(restos) < 2:
        return 1
    # se a lista de restos tiver mais de um numero, retorna o penultimo (antes do 0)
    else:
        return restos[-2]








n = 1
print(gcdOfOddEvenSums(n))
def differenceOfSums(n, m):
    # Inicia as variáveis que irão ter os números divisiveis e não divisiveis
    somaDivisiveis = 0
    somaNaoDivisiveis = 0

    # Laço que percorre do 1 até o numero (n+1 pois se não irá apenas do 0 até o numero)
    for i in range(1, n+1):
        # Se for possível sobrar 0 em uma divisão do número por m
        if i % m == 0:
            # Soma o número nos numeros divisiveis
            somaDivisiveis += i
        # Senão, soma os números nos numeros não divisiveis
        else:
            somaNaoDivisiveis += i

    # Retorna a subtração entre os dois 
    return(somaNaoDivisiveis - somaDivisiveis)








n = 10
m = 3
print(differenceOfSums(n,m))
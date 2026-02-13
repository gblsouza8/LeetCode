def commonFactors(a, b):

    # conta cada numero que divide ambos
    contador = 0
    # percorre os numeros inteiros até b
    for i in range(1, b+1):
        # se a sobra da divisão de a por i e de b por i for 0, incrementa o contador
        if a % i == 0 and b % i == 0:
            contador += 1
    # retorna o contador
    return contador







a = 12
b = 6
print(commonFactors(a, b))
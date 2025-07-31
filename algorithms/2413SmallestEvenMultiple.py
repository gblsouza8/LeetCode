def smallestEventMultiple(n):
    # Listas que irão salvar os multiplos dos números
    multiplosn = []
    multiplos2 = []

    # Máximo de vezes que irá multiplicar os números
    max = 300

    # Multiplica e armazena na lista
    for i in range(max):
        multiplosn.append(i*n)

    for i in range(1,max):
        multiplos2.append(i*2)


    # Compara se o indice atual de multiplosn está em multiplos2, se estiver, retorna ele
    for i in range(len(multiplosn)):
        if multiplosn[i] in multiplos2:
            return multiplosn[i]


n = 101
print(smallestEventMultiple(n))
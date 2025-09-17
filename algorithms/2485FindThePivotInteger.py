def pivotInteger(n):

    # variaveis q serão usadas
    x = 0
    y = 0


    # percorre todos os digitos de 1 até n
    for i in range(1, n+1):
        print(i)

        # reseta x para 0
        x = 0

        # encontra o valor de x (soma dos numeros de 0 até i)
        for j in range(i+1):
            x += j

        # reseta y para 0
        y = 0
        # encontra o valor de y (soma dos numeros de i até n)
        for l in range(i, n+1):
            y += l


        # se x tiver o mesmo valor que y, retorna i
        if x == y:
            return i
        
    # se sair do laço sem ter retornado nada, retorna -1
    return -1
            
        



        


n = 8
print(pivotInteger(n))
def mirrorDistance(n):

    # inverte n
    numero_invertido = int(str(n)[::-1])
    # retorna n - a versão invertida
    return abs(n - numero_invertido)
    

n = 25
print(mirrorDistance(n))
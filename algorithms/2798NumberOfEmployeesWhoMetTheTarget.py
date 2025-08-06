def numberOfEmployees(hours, target):
    # Inicializa o contador
    contador = 0

    # Percorre a lista de horas
    for i in range(len(hours)):
        # Se o indice atual for maior que o alvo, incrementa o contador
        if hours[i] >= target:
            contador += 1
    # Retorna o contador
    return contador

    

hours = [0,1,2,3,4]
target = 2
print(numberOfEmployees(hours, target))
def countCompleteDayPairs(hours):


    # variavel contador
    contador = 0

    # percorre as horas
    for i in range(len(hours)):
        
        for j in range(len(hours)):
            # caso i for diferente de j e menor que j
            if i != j and i < j:
                # caso a soma seja divisivel por 24, incrementa contador
                if (hours[i] + hours[j]) % 24 == 0:
                    contador += 1

    # retorna contador
    return contador




hours = [12,12,30,24,24]
print(countCompleteDayPairs(hours))
def earliestTime(tasks):


    # declaração das variaveis que serão usadas
    soma = 0
    # menor será a primeira soma para comparar 
    menor = tasks[0][0] + tasks[0][1]



    # percorre as tasks
    for i in range(len(tasks)):
        # reinicia soma para 0 a cada volta no laço
        soma = 0

        # soma cada valor da lista da task atual
        for j in range(len(tasks[i])):
            soma += tasks[i][j]


        # se o resultado final da soma for menor que o menor atual, atribui o valor de soma para menor
        if soma < menor:
            menor = soma


    # retorna menor
    return menor





tasks = [[1,6],[2,3]]
print(earliestTime(tasks))
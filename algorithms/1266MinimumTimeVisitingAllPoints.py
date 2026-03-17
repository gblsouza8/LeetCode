def minTimeToVisitAllPoints(points):

    # variavel para contar os segundos
    segundos = 0

    # percorre os pontos
    for i in range(len(points)-1):

        # encontra a maior diferença entre os pontos 
        maiorDiff = abs(points[i][0] - points[i+1][0])
        if abs(points[i][1] - points[i+1][1]) > maiorDiff:
            maiorDiff = abs(points[i][1] - points[i+1][1])
        # incrementa segundos com a maior diferença
        segundos += maiorDiff

    # retorna segundos
    return segundos






points = [[3,2],[-2,2]]
print(minTimeToVisitAllPoints(points))
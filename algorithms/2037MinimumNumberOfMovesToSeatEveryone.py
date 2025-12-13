def minMovesToSeat(seats, students):
    # variavel que será retornada
    movimentos = 0

    # ordena as listas em ordem decrescente para a subtração ser do maior de uma com o maior da outra
    seats.sort(reverse=True)
    students.sort(reverse=True)

    # percorre as listas
    for i in range(len(seats)):
        # soma cada subtração (usando abs() para manter o número positivo)
        movimentos+=abs(students[i]-seats[i])

    # retorna a soma dos movimentos
    return movimentos





seats = [4,1,5,9]
students = [1,3,2,6]
print(minMovesToSeat(seats, students))
def countStudents(students, sandwiches):


    while True:

        # se o primeiro da lista de students e de sandwiches for igual, deleta ambos da lista
        if students[0] == sandwiches[0]:
            del students[0]
            del sandwiches[0]
        else:
            # se for diferente, move o primeiro valor de students para o final (o adicionando no final e deletando do começo)
            students.append(students[0])
            del students[0]

        # caso o tamanho de students seja 0, sai do laço while
        if len(students) == 0:
            break
        
        # caso o sandwiches atual não esteja em students (não há mais estudante para aquele sanduiche), sai do laço while
        if sandwiches[0] not in students:
            break

    # retorna o tamanho de students ao sair do laço while
    return len(students)



students = [1,1,1,0,0,1]
sandwiches = [1,0,0,0,1,1]
print(countStudents(students, sandwiches))
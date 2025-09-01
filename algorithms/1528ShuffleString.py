def restoreString(s, indices):

    # variavel string que será retornada
    string2 = ""


    # percorre os indices
    for i in range(len(indices)):
        # procura nos indices o valor de i atual
        for j in range(len(indices)):
            # adiciona na string2 ao achar o caractere equivalente ao i atual (0 na lista indices e i 0, por exemplo)
            if indices[j] == i:
                string2 += s[j]

    # retorna string2
    return string2





s = "codeleet"
indices = [4,5,6,7,0,2,1,3]
print(restoreString(s, indices))
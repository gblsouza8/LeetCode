def selfDividingNumbers(left, right):

    # lista de numeros que serão retornados
    numeros = []

    # percorre os valores de left até right (+1 para chegar até o fim de right)
    for i in range(left, right+1):
        # transforma o i atual em uma string para percorrer todos os digitos
        string = str(i)
        # flag que verifica se passou na verificação em todos os digitos ou não
        verificador = True

        # percorre os digitos da string
        for j in range(len(string)):
                # verifica se não tem 0 nos digitos do número atual
                if '0' not in string:
                    # se a sobra de i dividido pelo digito atual for diferente de 0, muda a flag para False
                    if i % int(string[j]) != 0:
                        verificador = False
                    # se após a verificação, a flag for False, ignora o restante dos digitos e sai do loop j
                    if verificador == False:
                        break
                # se tiver 0 na string atual, já muda o verificador para False
                else:
                     verificador = False

        # caso termine o loop com o verificador ainda sendo True, adiciona o numero atual em numeros
        if verificador == True:
            numeros.append(i)
    
    # retorna os numeros após percorrer todos os números no alcance
    return numeros








left = 1
right = 22
print(selfDividingNumbers(left, right))
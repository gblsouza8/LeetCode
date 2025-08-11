def findPermutationDifference(s, t):

    # inicializa a lista que salvará a subtração das contas e a variavel que irá ser retornada
    lista = []
    soma = 0


    # percorre a string s
    for i in range(len(s)):
        # percorre a string t
        for j in range(len(t)):
            # compara o indice atual da string t com o indice atual da string 
            if t[j] == s[i]:
                # adiciona a subtração (arredondado) na lista
                lista.append(abs(i - j))

    # percorre a lista 
    for i in range(len(lista)):
        # adiciona todos os valores da lista em soma
        soma += lista[i]



    # retorna a soma
    return soma



s = "abc"
t = "bac"
print(findPermutationDifference(s, t))
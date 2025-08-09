def reverseDegree(s):
    # Listas com o alfabeto e seus devidos valores
    alfabeto = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
    valores = [26, 25, 24, 23, 22, 21, 20, 19, 18, 17, 16, 15, 14, 13, 12, 11, 10, 9, 8, 7, 6, 5, 4, 3, 2, 1]
    # Variável que irá salvar a soma e ser retornada
    soma = 0

    # Percorre a string
    for i in range(len(s)):
        # Define que x sempre será o indice atual + 1 para realizar a multiplicação
        x = i+1
        # Percorre a lista do alfabeto procurando pelo caractere atual em s
        for j in range(len(alfabeto)):
            # Quando encontra, soma e multiplica por x (indice atual da string)
            if s[i] == alfabeto[j]:
                soma += valores[j] * x

    # Retorna a soma 
    return soma





s = "abc"
print(reverseDegree(s))

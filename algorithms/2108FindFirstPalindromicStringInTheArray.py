def firstPalindrome(words):

    # percorre as palavras na lista
    for i in range(len(words)):


        # define uma variavel string vazia para inverter a palavra atual
        palavraInvertida = ""
        # monta a string usando um laço for invertido
        for j in range(len(words[i]) - 1, -1 , -1):
            palavraInvertida += words[i][j]
            

        # se a palavrainvertida for igual a palavra atual, retorna ela
        if palavraInvertida == words[i]:
            return words[i]
    
    # se sair do laço sem retornar nenhuma palavra, retorna uma string vazia
    return ""


        

words = ["abc","car","ada","racecar","cool"]
print(firstPalindrome(words))
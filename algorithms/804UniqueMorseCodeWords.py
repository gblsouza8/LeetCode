def uniqueMorseRepresentations(words):


    # inicialização das variaveis que serão usadas
    listaMorse = []
    unicos = []
    string = ""
    alfabetoMorse = [".-","-...","-.-.","-..",".","..-.","--.","....","..",".---","-.-",".-..","--","-.","---",".--.","--.-",".-.","...","-","..-","...-",".--","-..-","-.--","--.."]
    alfabeto = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']


    # percorre a lista de palavras
    for i in range(len(words)):

        # reinicia a string para uma versao vazia
        string = "" 
        # percorre os caracteres da palavra atual
        for j in range(len(words[i])):
            # procura o caractere atual em alfabeto
            for x in range(len(alfabeto)):
                if words[i][j] == alfabeto[x]:
                    # adiciona na string a versão em morse do caractere
                    string += alfabetoMorse[x]
        # após sair do laço da palavra, adiciona ela na lista em morse
        listaMorse.append(string)
                    


    # percorre a lista de palavras traduzidas
    for i in range(len(listaMorse)):
        # se a palavra nao estiver na lista de palavras unicas, adiciona ela
        if listaMorse[i] not in unicos:
            unicos.append(listaMorse[i])

    # retorna a quantidade de indices na lista de palavras unicas
    return len(unicos)





words = ["gin","zen","gig","msg"]
print(uniqueMorseRepresentations(words))
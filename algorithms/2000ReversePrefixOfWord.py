def reversePrefix(word, ch):


    # verifica se a palavra contém o caractere, se tiver, ja retorna a palavra imediatamente
    if ch not in word:
        return word


    # inicia a variavel que irá formar a palavra até o caractere desejado aparecer
    pac = ""
    # variavel que irá salvar a palavra invertida
    reverse = ""
    # variavel que irá armazenar o indice onde o caractere foi encontrado
    x = 0
    # percorre a palavra
    for i in range(len(word)):
        # se o indice atual for o caractere
        if word[i] == ch:
            # adiciona na variavel com as letras até o indice
            pac += word[i]
            # define que x será o indice atual (onde o caractere foi encontrado)
            x = i
            # finaliza o laço
            break
        # se não, apenas adiciona a letra na variavel
        else:
            pac += word[i]


    # percorre a string com as letras até o caractere para montar uma versao invertida dele
    for i in range(len(pac) - 1, -1, -1):
        reverse += pac[i]

    # adiciona na versao invertida as letras que faltaram a partir do indice salvo na variavel x
    for i in range(x+1, len(word)):
        reverse += word[i]


    # retorna a string final 
    return reverse

word = "abcdefd"
ch = "z"
print(reversePrefix(word, ch))
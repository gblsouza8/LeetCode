def truncateSentence(s, k):

    # variavel que irá armazenar a nova string
    ns = ""
    # contador de espaços
    contador = 0

    # percorre a palavra
    for i in range(len(s)):
        # a cada espaço encontrado, incrementa o contador
        if s[i] == " ":
            contador += 1
        # se contador for igual a k, irá sair do laço 
        if contador == k:
            break
        # se não, adicionará o caractere atual na nova string
        else:
            ns += s[i]

    # retorna a string   
    return ns


s = "Hello how are you Contestant"
k = 4
print(truncateSentence(s, k))
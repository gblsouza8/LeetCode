def countKeyChanges(s):

    # transforma a string inteira em lowercase para não diferenciar letras maiusculas e minisculas
    s = s.lower()
    # variavel contador que será incrementada a cada alteração
    contador = 0
    # percorre a string a partir do indice 1, porque não tem nada antes do indice 0
    for i in range(1, len(s)):
        # se o valor atual for diferente do valor anterior, incrementa o contador
        if s[i] != s[i-1]:
            contador += 1
    # retorna o contador
    return contador



s = "AaAaAaaA"
print(countKeyChanges(s))
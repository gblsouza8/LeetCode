def defangIPaddr(address):
    # Inicializa a variavel que vai ser utilizada mudar a string
    string = ""
    # Percorre a string
    for i in range(len(address)):
        # Verifica se o caractere atual é ".", se for, irá reescrever o . com [] antes e depois
        if address[i] == ".":
            string += "[.]"
        else:
        # Se não for, é apenas um número e irá coloca-lo na string normalmente
            string += address[i]

    # Retorna a string final 
    return string




address = "1.1.1.1"
print(defangIPaddr(address))
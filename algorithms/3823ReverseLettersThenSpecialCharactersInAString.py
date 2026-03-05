def reverseByType(s):


    # lista com as letras do alfabeto que podem user encontradas nas strings
    letras = ["a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m", "n", "o", "p", "q", "r", "s", "t", "u", "v", "w", "x", "y", "z" ]
    
    # string com a ordem do tipo de caractere para inserir em retorno
    ordemstring = ""

    # string que será retornada
    retorno = ""

    # array com as letras da string
    letrasinvertido = []
    # array com os caracteres especiais da string
    caracteresinvertido = []

    # monta as arrays e a ordem dos caracteres 
    for i in range(len(s)):
        if s[i] in letras:
            letrasinvertido.append(s[i])
            ordemstring += 'l'
        else:
            caracteresinvertido.append(s[i])
            ordemstring += 'c'


    # inverte as arrays
    letrasinvertido.reverse()
    caracteresinvertido.reverse()

    # monta a nova string usando como base a ordem dos caracteres
    for i in range(len(ordemstring)):
        if ordemstring[i] == 'l':
            # adiciona a primeira letra da array e a deleta da array para evitar o erro out of range
            retorno += letrasinvertido[0]
            del letrasinvertido[0]
        else:
            # adiciona o primeiro caractere especial da array e deleta da array
            retorno += caracteresinvertido[0]
            del caracteresinvertido[0]

    # retorna a string
    return retorno





s = ")ebc#da@f("
print(reverseByType(s))
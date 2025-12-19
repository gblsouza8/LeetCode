def freqAlphabets(s):
    
    # lista com as letras que utilizam apenas um digito
    alfabeto1 = ["a", "b", "c", "d", "e", "f", "g", "h", "i"]
    # lista com as letras que utilizam três digitos
    alfabeto2 = ["j", "k", "l", "m", "n", "o", "p", "q", "r", "s", "t", "u", "v", "w", "x", "y", "z"]
    # listas com os digitos
    digitos1 = ["1", "2", "3", "4", "5", "6", "7", "8", "9"]
    digitos2 = ["10#", "11#", "12#", "13#", "14#", "15#", "16#", "17#", "18#", "19#", "20#", "21#", "22#", "23#", "24#", "25#", "26#"]
    

    # procura primeiro as letras que utilizam três digitos
    for i in range(len(digitos2)):
        # se encontrar os digitos na string, substitui todas as ocorrencias dele pelo valor de memso indice em alfabeto2
        if digitos2[i] in s:
            s = s.replace(digitos2[i], alfabeto2[i])
                    
        
    # após substituir as letras que utilizam três digitos, procura as letras que utilizam apenas um
    for i in range(len(digitos1)):
        # se encontrar o digito na string, substitui todas as ocorrencias
        if digitos1[i] in s:
            s = s.replace(digitos1[i], alfabeto1[i])

    # retorna a string
    return s
        

s = "824#15#826#"
print(freqAlphabets(s))
def isPalindrome(x):
    texto = str(x)
    textoInvertido = texto[::-1]
    return(texto == textoInvertido)

x = 121
print(isPalindrome(x))
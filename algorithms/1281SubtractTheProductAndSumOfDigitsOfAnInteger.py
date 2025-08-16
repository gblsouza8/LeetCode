def subtractProductAndSum(n):
    # variaveis soma e multiplicação que serão incrementadas nos laços for
    soma = 0
    mult = 1
    # converte o inteiro para string para conseguir percorrer os digitos
    string = str(n)


    # laço para conseguir a soma dos digitos
    for i in range(len(string)):
        # transforma o caractere atual em int de volta e soma com a variavel soma
        soma += int(string[i])

    # laço para conseguir a multiplicação dos digitos
    for i in range(len(string)):
       # transforma o caractere atual em int de volta e multiplica pelo valor atual de mult
       mult = mult * int(string[i])


    # retorna a subtração de ambos
    return mult - soma 


n = 234
print(subtractProductAndSum(n))
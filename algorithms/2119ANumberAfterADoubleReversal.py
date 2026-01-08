def isSameAfterReversal(num):
    
    # transforma o valor em string para poder inverter
    string = str(num)
    
    # repete o bloco de código 2x
    for i in range(2):
        # versão inversa da string
        string2 = string[::-1]
        # transforma em int
        num2 = int(string2)
        # redefine o valor da variavel string para o valor atual, para poder reiniciar o bloco
        string = str(num2)
    return num == num2


num = 1800
print(isSameAfterReversal(num))
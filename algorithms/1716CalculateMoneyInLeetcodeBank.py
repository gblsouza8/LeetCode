def totalMoney(n):

    # variavel que será retornada
    soma = 0
    # variavel que conta as semanas para adicionar o valor extra
    semana = 0

    # enquanto n (quantidade de dias) for maior que 0 
    while n > 0:

        # caso n seja menor que 7
        if n < 7:
            # a partir de 1, vai até n+1
            for i in range(1, n+1):
                # adiciona o valor extra da semana em soma
                soma+=semana
                # incrementa soma
                soma+=i
                # tira um de n (dias restantes)
                n-=1
        # caso o n seja maior que 7, irá tirar 7 dias de uma vez
        else:
            for i in range(1, 7+1):
                # adiciona o valor extra da semana em soma
                soma += semana
                # incrementa soma
                soma += i
                # subtrai 1 dia de n
                n-=1

        # depois de sair dos for, incrementa semana
        semana += 1
    # retorna soma após sair do while (n = 0)
    return soma




n = 10
print(totalMoney(n))
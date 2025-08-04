def minBitFlips(start, goal):
    # Inicializa as variáveis que salvarão as versões binárias dos números
    start_binario = ""
    goal_binario = ""

    # Forma a versão binária de start
    string = ""
    x = start
    while int(x) > 0:
        string += str(int(x%2))
        x = x / 2
    
    # Digita a string ao contrário
    for i in range(len(string) -1, -1, -1):
        start_binario += string[i]


    # Forma a versão binária de goal
    string = ""
    x = goal
    while int(x) > 0:
        string += str(int(x%2))
        x = x / 2
    
    # Digita a string ao contrário
    for i in range(len(string) -1, -1, -1):
        goal_binario += string[i]


    # Adiciona zero's em caso de um número ser maior que o outro ou não reconhecer o 0 inicial
    if len(start_binario) > len(goal_binario):
        diff = len(start_binario) - len(goal_binario)
        for i in range(diff):
            goal_binario = "0" + goal_binario
    elif len(start_binario) < len(goal_binario):
        diff = len(goal_binario) - len(start_binario)
        for i in range(diff):
            start_binario = "0" + start_binario


    # Inicializa o contador de passos
    contador = 0
    # Percorre a lista do último indice até o primeiro
    for i in range(len(goal_binario) -1, -1, -1):
        # Se o indice atual for igual em ambas as listas, não faz nada
        if start_binario[i] == goal_binario[i]:
            pass
        # Se forem diferentes, substitui o indice no valor start e incrementa o contador
        else:
            if start_binario[i] == "1":
                if i < len(goal_binario) - 1:
                    start_binario = start_binario[:i] + "0" + start_binario[i+1]
                else: 
                    start_binario = start_binario[:i] + "0"
            elif start_binario[i] == "0":
                if i < len(goal_binario) -1:
                    start_binario = start_binario[:i] + "1" + start_binario[i+1]
                else: 
                    start_binario = start_binario[:i] + "1"
            contador += 1


    # Retorna o contador
    return contador

start = 3
goal = 4
print(minBitFlips(start, goal))
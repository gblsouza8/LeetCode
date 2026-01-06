def finalPositionOfSnake(n, commands):

    # variavel que mudará com os movimentos
    atual = 0
    
    # percorre os comandos
    for i in range(len(commands)):
        # caso o comando seja RIGHT, soma 1
        if commands[i] == "RIGHT":
            atual += 1
        # caso o comando seja DOWN, soma n 
        elif commands[i] == "DOWN":
            atual += n
        # caso o comando seja UP, subtrai n
        elif commands[i] == "UP":
            atual -= n
        # caso o comando seja LEFT, subtrai 1
        elif commands[i] == "LEFT":
            atual -= 1

    # retorna a posição atual
    return atual
n = 2
commands = ["RIGHT","DOWN"]
print(finalPositionOfSnake(n, commands))
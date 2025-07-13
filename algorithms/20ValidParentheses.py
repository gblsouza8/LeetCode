def isValid(s):
    pilha = [] 
    combinacoes = {')': '(', '}': '{', ']': '['}

    for char in s:
        if char in '({[':
            pilha.append(char)
        elif char in ')}]':
            if not pilha or pilha[-1] != combinacoes[char]:
                return False
            pilha.pop()

    return len(pilha) == 0


s = "[([]])"
print(isValid(s))

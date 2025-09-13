def checkIfPangram(sentence):
    letras = []
    alfabeto = ["a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m", "n", "o", "p", "q", "r", "s", "t", "u", "v", "w", "x", "y", "z"]


    for i in range(len(sentence)):
        if sentence[i] not in letras:
            letras.append(sentence[i])
        
    if len(letras) == len(alfabeto):
        return True
    else:
        return False
    




sentence = "thequickbrownfoxjumpsoverthelazydog"
print(checkIfPangram(sentence))
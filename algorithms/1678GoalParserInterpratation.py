def interpret(command):
    str = ""
    for i in range (len(command)):
        if i < len(command):
            if command[i] == "(":
                if command[i+1] == ")":
                    str += "o"
                if command [i+1] == "a":
                    str += command[i+1]
                    str += command[i+2]
            elif command[i] == "G":
                str += "G"



    return str










command = "G()()()()(al)"
print (interpret(command))
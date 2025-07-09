'''
Given an array of integers nums and an integer target, return indices of the two numbers such that they add up to target.

You may assume that each input would have exactly one solution, and you may not use the same element twice.

You can return the answer in any order.
'''

def twoSum(nums, target):
    # Pega o tamanho da lista para usar no laço for
    tamanho = len(nums)
    # Inicia a variável que armazenará os indices do resultado
    resultado = []
    # Try para ignorar o erro out of index
    try: 
        # Inicia o laço for para percorrer a lista 
        for i in range(tamanho):
                # Inicia outro laço for, para comparar o i (indice atual) com o j (outros indices da lista)
                for j in range(tamanho):
                     # Verifica se está comparando o indice atual com ele mesmo, caso esteja, quebra o loop atual
                     if i == j:
                          break
                     # Caso não esteja, compara e se o resultado da soma for o alvo, armazena ambos os indices na lista
                     elif nums[i] + nums[j] == target:
                          resultado.append(i)
                          resultado.append(j)
    # Except e pass para ignorar o possível erro out of index
    except:
        pass
    # Retorna o resultado
    return(resultado)




# Variáveis de teste
nums = [3,2,3]
target = 6
print(twoSum(nums, target))

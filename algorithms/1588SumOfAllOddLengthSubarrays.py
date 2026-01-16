def sumOddLengthSubarrays(arr):


    contador = 0

    for i in range(len(arr)+1):

        if i % 2 != 0:
            for j in range(0, len(arr)-i +1):
                contador += sum(arr[j:j + i])
    return contador





arr = [1,4,2,5,3]
print(sumOddLengthSubarrays(arr))
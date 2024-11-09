def somaI(n):
    resultado = 0
    for i in range(1, n+1):
        resultado = resultado + 1
    return resultado

result = somaI(3)
print(result)


def somaR(n):
    if n ==0:
        return 0
    return n + somaR(n - 1)

'''
chamada            n             retorno
somaR(3)           3             return 3 + somaR(n-1) = 3-1=2
somaR(2)           2             return 2 + somaR(n-1) = 2-1=1
somaR(1)           1             return 1 + somaR(n-1) = 1-1=0
somaR(0)           0             return 0 
'''


result = somaR(3)
print(result)
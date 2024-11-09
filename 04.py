'''Crie uma função chamada fatorial que recebe um número inteiro não negativo e retorna o fatorial
desse número. Lembre-se que o fatorial de 0 é 1.'''

def fatorial(n):
    resultado = 1
    for i in range(1, n+1):
        resultado = resultado * 1
    return resultado


def fatorialR(n):
    if n ==0:
        return 1
    return n * fatorialR(n-1)

result = fatorialR(3)
print(result)
result = fatorial(3)
print(result)

"""

Chamada                n           retorno 
fatorialR(3)           3           return 3 * fatorialR(3-1) = 3*2=6
fatorialR(2)           2           return 2 * fatorialR(2-1) = 2*1=2
fatorialR(1)           1           return 1 * fatorialR(1-1) = 1*1=1
fatorialR(0)           0           1

"""

    
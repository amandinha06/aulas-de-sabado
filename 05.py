'''Escreva uma função chamada eh_primo que recebe um número inteiro e retorna True se o número
for primo e False caso contrário.'''


def eh_primo(n):
    if n <= 1:
        return False 
    if n <= 3:
        return True 

    i = 5
    while i * i <= n:
        if n % i == 0 or n % (i + 2) == 0:
            return False
        i += 6

    return True

print(eh_primo(17))
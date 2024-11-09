'''Desenvolva uma função chamada conta_vogais que recebe uma string e retorna o número de vogais
(a, e, i, o, u) presentes na string.'''

def conta_vogais(texto):
    vogais = "aeiouAEIOU"
    contador = 0

    for letra in texto:
        if letra in vogais:
            contador += 1

    return contador

texto = "Olá, mundo! Como você está?"
numero_vogais = conta_vogais(texto)
print("O número de vogais é:", numero_vogais)

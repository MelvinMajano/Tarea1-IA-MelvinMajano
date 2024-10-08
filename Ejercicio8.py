def contarvocales(cadena):
    c=0
    vocales = 'aeiouAEIOU'

    for letra in cadena:
        if letra in vocales:
            c+=1
    return c

print('Ingrea una cadena texto')
cadena = input()

numeroVocales = contarvocales(cadena)
print(f'El numero de vocales en la cadena es: {numeroVocales}')

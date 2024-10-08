
import random
import string

print(f'Ingrese la logitud de la cadena')
logitud= int(input())

cadena =''
caracteres = string.ascii_letters + string.digits + string.punctuation
for i in range(10):
    letra = random.choice(caracteres)
    cadena+=letra
print(cadena)
import random


numero=random.randint(1,100)
c=0


numeroUsuario=int(input("¡Adivina el número entre 1 y 100!"))

while numeroUsuario != numero:
     c+=1
     if numeroUsuario < numero :
         print('El número es mayor.')
         numeroUsuario = int(input("Ingresa tu intento: "))
     elif numeroUsuario > numero:
         print('El número es menor.')
         numeroUsuario = int(input("Ingresa tu intento: "))

print(f'¡Felicitaciones! Has adivinado el número en {c + 1 } intentos')


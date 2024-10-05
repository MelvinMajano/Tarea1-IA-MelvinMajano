
class Libro:
    def __init__(self,titulo,autor,anio_publicacion,numero_paginas):
        self.titulo=titulo
        self.autor=autor
        self.anio_publicacion=anio_publicacion
        self.numero_paginas=numero_paginas

    def mostrar_informacion(self):
        print("Titulo:",self.titulo,"Autor:",self.autor,"Anio de publicacion:",self.anio_publicacion,"Numero de paginas:",self.numero_paginas)


libro=Libro('Harry Potter y la piedra filosofal','J. K. Rowling',1997,309)

libro.mostrar_informacion()
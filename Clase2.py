from Clase1 import Material

class Libro(Material):
    def __init__(self, titulo, autor, precio, paginas):
        super().__init__(titulo, autor, precio)
        self.paginas = paginas

    def descripcion(self):
        """Devuelve descripción específica de un libro"""
        return f"Libro: {self.titulo}, Autor {self.autor}, Páginas {self.paginas}"

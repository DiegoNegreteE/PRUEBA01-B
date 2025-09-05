class Material:
    def __init__(self, titulo, autor, precio):
        self.titulo = titulo
        self.autor = autor
        self.__precio = precio  # atributo encapsulado

    def get_precio(self):
        """Retorna el precio del material"""
        return self.__precio

    def set_precio(self, nuevo_precio):
        """Cambia el precio solo si es mayor a 0"""
        if nuevo_precio > 0:
            self.__precio = nuevo_precio

    def descripcion(self):
        """Devuelve una descripción general del material"""
        return f"Material: Título {self.titulo}, Autor {self.autor}"

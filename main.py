# Clase base Material
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


# Clase hija Libro
class Libro(Material):
    def __init__(self, titulo, autor, precio, paginas):
        super().__init__(titulo, autor, precio)
        self.paginas = paginas

    def descripcion(self):
        """Devuelve descripción específica de un libro"""
        return f"Libro: {self.titulo}, Autor {self.autor}, Páginas {self.paginas}"


# Clase hija Revista
class Revista(Material):
    def __init__(self, titulo, autor, precio, edicion):
        super().__init__(titulo, autor, precio)
        self.edicion = edicion

    def descripcion(self):
        """Devuelve descripción específica de una revista"""
        return f"Revista: {self.titulo}, Autor {self.autor}, Edición {self.edicion}"


# Clase hija Periodico
class Periodico(Material):
    def __init__(self, titulo, autor, precio, fecha_publicacion):
        super().__init__(titulo, autor, precio)
        self.fecha_publicacion = fecha_publicacion

    def descripcion(self):
        """Devuelve descripción específica de un periódico"""
        return f"Periódico: {self.titulo}, Autor {self.autor}, Fecha {self.fecha_publicacion}"


# Clase Biblioteca
class Biblioteca:
    def __init__(self):
        self.catalogo = []

    def agregar_material(self, material):
        """Agrega un material al catálogo"""
        self.catalogo.append(material)

    def mostrar_catalogo(self):
        """Muestra la descripción y precio de cada material y calcula el total"""
        total = 0
        for material in self.catalogo:
            print(material.descripcion(), "- Precio:", material.get_precio())
            total += material.get_precio()
        print(f"\nValor total del catálogo: {total}")


# Programa principal (main)
if __name__ == "__main__":
    # Crear la biblioteca
    biblioteca = Biblioteca()

    # Instanciar materiales
    libro = Libro("El Quijote", "Cervantes", 10000, 800)
    revista = Revista("National Geographic", "Varios", 5000, 220)
    periodico = Periodico("El Mercurio", "Redacción", 1000, "04/09/2025")

    # Usar el setter para modificar el precio
    libro.set_precio(12000)

    # Agregar materiales a la biblioteca
    biblioteca.agregar_material(libro)
    biblioteca.agregar_material(revista)
    biblioteca.agregar_material(periodico)

    # Mostrar catálogo
    biblioteca.mostrar_catalogo()

    """
    Explicaciones de los conceptos trabajados:
    - Relación padre-hijo: Libro, Revista y Periódico heredan de Material.
    - Polimorfismo: Cada clase sobrescribe el método descripcion() de manera distinta.
    - El main crea los objetos, modifica un precio con el setter, los agrega a la biblioteca y muestra el catálogo.
    """

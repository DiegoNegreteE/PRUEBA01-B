from Clase2 import Libro
from Clase3 import Revista
from Clase4 import Periodico
from ClaseN import Biblioteca

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
    Explicaciones:
    - Relación padre-hijo: Libro, Revista y Periódico heredan de Material.
    - Polimorfismo: Cada clase sobrescribe el método descripcion() de manera distinta.
    - El main crea los objetos, modifica un precio con el setter, los agrega a la biblioteca y muestra el catálogo.
    """

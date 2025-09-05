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

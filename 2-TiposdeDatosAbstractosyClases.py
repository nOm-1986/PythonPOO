''' TIPOS DE DATOS ABSCTRACTOS

    - En python todo es un objeto y tiene un tipo.
        - Representación de datos y formas de interactuar con ellos.

    - Formas de interactura con un objeto:
        - Creación
        - Manipulación
        - Destrucción

    - Ventajas:
        - Decomposición.
        - Abstracción
        - Encapsulación.
    
    INSTANCIAS
        - Mientras que la clase es un molde, a los objetos cre
    
    Saber si lo que pasamos es instancia de algo: isinstance()
'''


class Coordenada:

    def __init__(self, x, y):
        self.x = x
        self.y = y

    def distancia(self, otra_coordeanda):
        x_diff = (self.x - otra_coordeanda.x)**2
        y_diff = (self.y - otra_coordeanda.y)**2
        
        return (x_diff + y_diff)**0.5


if __name__== '__main__':
    coord_1 = Coordenada(3, 30)
    coord_2 = Coordenada(4, 8)
    print(coord_1.distancia(coord_2))
    print(isinstance(coord_2, Coordenada))
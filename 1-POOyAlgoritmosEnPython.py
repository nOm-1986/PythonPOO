'''
    COURSE OBJETIVES
    1 - Entender cómo funciona la Programación Orientada a Objectos.
    2 - Entender cómo medir la eficiencia temporal y espacial de nuestros algoritmos.
    3 - Entender cómo y por qué graficar.
    4 - Aprender a resolver problemas de búsqueda, ordenación y optimización.


    a - Para definir una clase en python utilizamos la palabra reservada class <nombre de la clase>
        class Hotel:
    

    b - La instanciamos
        hotel = Hotel()
    

    c - Constructor
        __init__(self, parametro1, parametro2, parametro3...).
        self = Primer parámetro obligatorio(que es simplemente una referencia a la instancia).

        class Hotel:
        
        def __init__(self, numero_maximo_de_huespedes, lugares_de_estacionamiento):
            self.numero_maximo_de_huespedes = numero_maximo_de_huespedes
            self.lugares_de_estacionamiento = lugares_de_estacionamiento
            self.huespedes = 0
    

    d - Métodos
        Los métodos son equivalentes a funciones dentro de la definición de la clase, pero todos reciben self como primer argumento.
        
        def anadir_huespedes(self, cantidad_de_huespedes):
            self.huespedes += cantidad_de_huespedes

        def checkout(self, cantidad_de_huespedes):
            self.huespedes -= cantidad_de_huespedes

        def ocupacion_total(self):
            return self.huespedes

        

'''
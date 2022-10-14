''' Abstracción

    - Enfocarnos en la información relevante.
    - Separar la información central de los detalles secundarios.
    - Podemos utilizar variables y métodos (privados o públicos)
    - _ para indicar que es un método privado, pero en python no existen método privados, es solo una convención.

'''

class Lavadora:
    
    def __init__(self):
        pass


    def lavar(self, temperatura='caliente'):
        self._llenar_tanque_de_agua(temperatura)
        self._anadir_jabon()
        self._lavar()
        self._centrifugar()


    def _llenar_tanque_de_agua(self, temperatura):
        print(f'Llenando el tanque con agua {temperatura}')


    def _anadir_jabon(self):
        print(f'Añadiendo jabon')
    

    def _lavar(self):
        print('Estoy lavando')


    def _centrifugar(self):
        print('Centrifugando')


if __name__ == '__main__':
    lavadora = Lavadora()
    #lavadora.lavar('templado')
    lavadora._anadir_jabon()
    lavadora._lavar()
    lavadora._centrifugar()
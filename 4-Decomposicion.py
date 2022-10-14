''' 4 - Decomposición
    - Partir un problema en problemas más pequeños.
    - Las clases permietn crear mayores abstracciones en forma de componentes.
    - Cada clase se encarga de una parte del problema y el programa se vuelve más fácil de mantener.
'''

class Automovil:
    
    def __init__(self, modelo, marca, color):
        self.modelo = modelo
        self.marca = marca
        self.color = color
        self._estado = 'en_reposo'
        # self._motor = None # None -> Que no tiene ningun valor.
        self._motor = Motor(4,'ACPM')


    def acelerar(self, tipo='despacio'):
        if tipo == 'rapido':
            self._motor.inyecta_gasolina(10)
        else:
            self._motor.inyecta_gasolina(4)


class Motor:

    def __init__(self, cilindros, tipo='gasolina'):
        self.cilindros = cilindros
        self.tipo = tipo
        self._temperatura = 0

    
    def inyecta_gasolina(self, cantidad):
        pass
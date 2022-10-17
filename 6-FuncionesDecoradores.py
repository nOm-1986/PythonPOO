''' 
FUNCIONES DECORADORAS

DEF: Forma sencilla de llamar funciones de orden mayor --> WTF??
    Funciones que toman otra función como parámetro y retornan otra función como resultado.
    De esta forma un decorador añade capacidades a una función sin modificarla.

Funciones como objetos de primera-clase
Es decir, pueden ser pasados y utilizados como argumentos al igual que cualquier otro objecto(strings, enteros, flotantes, listas, etc ).
'''

def presentarse(nombre):
	return f"Me llamo {nombre}"

def estudiemos_juntos(nombre):
	return f"¡Hey {nombre}, aprendamos Python!"

def calificar_docente(nombre):
    return f"¡Hey {nombre} no olvides calificar a tu profesor!"

def consume_funciones(funcion_entrante, nombre):
	return funcion_entrante(nombre)

def consume_funciones(funcion_ejecutar, parametro):
    return funcion_ejecutar(parametro)



'''

'''



if __name__ == '__main__':
    print(consume_funciones(estudiemos_juntos, 'José Fabián'), '\n')
    
    print(consume_funciones(calificar_docente, 'José Fabián'), '\n')
    
''' SETTERS, GETTERS Y Decorador property

'''

def funcion_decoradora(funcion):
	def wrapper():
		print("Este es el último mensaje...")
		funcion()
		print("Este es el primer mensaje ;)")
	return wrapper

def zumbido():
	print("Buzzzzzz")

zumbido = funcion_decoradora(zumbido)

"""
Si no diste con el resultado no te preocupes, solo hay que analizarlo con detalle 
y el truco está en la línea zumbido = funcion_decoradora(zumbido). 
Sucede que la función wrapper() recibió la función zumbido() como parámetro y coloca su 
salida entre los otros dos prints.

Todo lo que sucede se conoce en programación como metaprogramación (metaprogramming), 
ya que una parte del programa trata de modificar a otra durante el tiempo de compilación. 
En tanto, un decorador básicamente toma una función, le añade alguna funcionalidad y la retorna.
"""
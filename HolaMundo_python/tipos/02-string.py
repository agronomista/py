nombre_curso = "Ultimate Python"

# en la linea posterior se puede escribir una cadena de texto prolongada presinando comillas triples
descripción_curso = """
Trabajo realizado para una prueba,
HolaMundo
"""
print(nombre_curso, descripción_curso)
# permite obtener la longitud del string se usa len y para ver el resultado print
# ojo, función-argumento, se usaron 2 funciones y la sintáxis anterior es la correcta
print(len(nombre_curso))
# acceder a un caracter en particular, uso de parentesis cuadrados
print(nombre_curso[3])
# rango de string a tomar
print(nombre_curso[0:8])
# para seleccionar desde donde comenzar
print(nombre_curso[9:])
# desde donde terminar
print(nombre_curso[:8])  # lo mismo que la linea 15

print(nombre_curso[:])

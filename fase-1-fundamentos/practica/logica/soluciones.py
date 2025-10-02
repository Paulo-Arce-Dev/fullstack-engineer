# Guia Ejercicios 1 - Lógica de programación

# Ejercicio 2
""" 
numero_usuario = int(input("Ingrese un numero por favor "))
numero_usuario_cubo = (numero_usuario * numero_usuario) * numero_usuario
print(f"El numero del usuario elevado al cubo es: {numero_usuario_cubo}")
"""

# Ejercicio 3
""" 
ano_actual = int(input("Ingrese el año actual por favor: "))
ano_nacimiento = int(input("Ingrese el año de su nacimiento por favor: "))
edad_usuario = ano_actual - ano_nacimiento
print(f"Su edad es de: {edad_usuario} anos")
"""

# Ejercicio 4
"""  
distancia_ciudades = float(input("Ingresa la distancia en KM que hay entre dos ciudades: "))
velocidad_promedio_vehiculo = float(input("Ingrese la velocidad promedio del vehiculo en el que viaja: "))
tiempo_aproximado_llegada = distancia_ciudades / velocidad_promedio_vehiculo
print(f"El tiempo aproximado de llegada es de: {tiempo_aproximado_llegada:.2f} horas")
"""

# Ejercicio 5
"""  
sueldo_fijo = 15000
comision = 5 / 100

total_facturado = float(input("Ingrese el total facturado por favor: "))
comision_aplicada = total_facturado * comision

sueldo_total = sueldo_fijo + comision_aplicada
print(f"El sueldo total a pagar es de: {sueldo_total} ARS")
"""

# Ejercicio 6
"""
primer_nota = int(input("Ingrese la nota de su primer examen: "))
segunda_nota = int(input("Ingrese la nota de su segundo examen: "))
tercera_nota = int(input("Ingrese la nota de su tercer examen: "))

promeido = (primer_nota + segunda_nota + tercera_nota) / 3 
print(f"Su promedio es de: {promeido:.2f}")
""" 

# Ejercicio 7
""" 
metros_cuadrados_totales = float(input("Ingresa los metros cuadrados de un predio: "))
metros_cubiertos = float(input("Ingresa los metros cuadrados cubiertos del predio: "))

#porcentaje de metros cubiertos
porcentaje_metros_cubiertos = (metros_cubiertos * 100) / metros_cuadrados_totales
print(f"Porcentaje de metros cubiertos del predio: {porcentaje_metros_cubiertos:.2f}%")

# porcentaje de metros descubiertos
porcentaje_metros_descubiertos = 100 - porcentaje_metros_cubiertos
print(f"El porcentaje de metros cuadrados desocupados del predio es de: {porcentaje_metros_descubiertos:.2f}%")
"""

# Ejercicio 8
"""  
descuento = 15 / 100

monto_total = float(input("Ingrese el monto total de la venta: "))
descuento_aplicado = monto_total * descuento

monto_cobrar = monto_total - descuento_aplicado
print(f"El total a cobrar con un 15% de descuento es de: ${monto_cobrar} ARS")
"""

# Ejercicio 9
"""  
mujeres = int(input("Ingrese la cantidad de mujeres en la carrera: "))
hombres = int(input("Ingrese la cantidad de hombres en la carrera: "))

# 100%
estudiantes_totales = mujeres + hombres

porcentaje_mujeres = (mujeres * 100) / estudiantes_totales
print(f"El porcentaje de muejres: {porcentaje_mujeres:.2f}%")

porcentaje_hombres = 100 - porcentaje_mujeres 
print(f"El porcentaje de hombres: {porcentaje_hombres:.2f}%")
"""

# Ejercicio 10
numero_uno = float(input("Ingrese un numero por favor: "))
numero_dos = float(input("Ingrese un segundo numero por favor: "))

suma = numero_uno + numero_dos
resta = numero_uno - numero_dos
multilicacion = numero_uno * numero_dos
division = numero_uno / numero_dos

print(f"Resultados de la suma: {suma:.2f}")
print(f"Resultados de la resta: {resta:.2f}")
print(f"Resultados de la multiplicacion: {multilicacion:.2f}")
print(f"Resultados de la division: {division:.2f}")
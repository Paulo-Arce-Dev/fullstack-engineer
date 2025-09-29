# Resolución de ejercicios - Variables


# Ejercicio 1 - Primera Variable
print("----- Ejercicio 1 -----")

nombre = 'Paulo'
print(nombre)


# Ejercicio 2 - Operaciones Simples
print("----- Ejercicio 2 -----")

a = 10
b = 3
resultado = a + b 


# Ejercicios 3 - Intercambio de Variables
print("----- Ejercicio 3 -----")

x = 5
y = 8

x = y
y = x 
print(x, y)


# Ejercicio 4 - Información Personal
print("----- Ejercicio 4 -----")

edad = 24
ciudad_de_nacimiento = "Villa Maria"
color_favorito = 'Amarillo'
print(f"Tengo {edad} de edad, naci en la ciudad {ciudad_de_nacimiento} y mi color favorito es el {color_favorito}")


# Ejercicio 5 - Cálculo de Área
print("----- Ejercicio 5 -----")

largo_rectangulo_cm = 16
ancho_rectangulo_cm = 9

area_rectangulo = largo_rectangulo_cm * ancho_rectangulo_cm
perimetro_rectangulo = (largo_rectangulo_cm * 2) + (ancho_rectangulo_cm * 2)

print(f"El area del rectangulo es de: {area_rectangulo}")
print(f"El perimetro del rectangulo es de: {perimetro_rectangulo}")


# Ejercicio 6 - Conversión de Temperatura
print("----- Ejercicio 6 -----")
# 1 °C es igaual a 33.8 Fahrenheit
# 1 °C es igaual a 274.15 Kelvin

temperatura_celcius = 10
conversion_a_fahrenheit = temperatura_celcius * 33.8
conversion_a_kelvin = temperatura_celcius * 274.15

print(f"Temperatura actual en Celcius: {temperatura_celcius} C")
print(f"Temperatura de Celcius a Fahrenheit: {conversion_a_fahrenheit} F")
print(f"Temperatura de Celcius a Kelvin: {conversion_a_kelvin} K")


# Ejercicio 7 - Datos del Estudiante
print("----- Ejercicio 7 -----")

nombre_estudiante = 'Guido'
edad_estudiante = 17
carrera_estudiante = 'Tecnicatura superior en programacion'
promedio = 6

if (promedio >= 6): 
  aprobado = True
else:
  aprobado = False

print(f"Soy {nombre_estudiante}, tengo {edad_estudiante} años")
print(f"Estudia la carrera: {carrera_estudiante} y mi promedio es de: {promedio}")
print(f"Estado del estudiante: {aprobado}")


# Ejercicio 8 - Calculadora de Descuento
print("----- Ejercicio 8 -----")

precio_producto = 80000
print(f"El precio del producto es de: ${precio_producto} ARS")

porcentaje_descuento = 8
print(f"El decuento obtenido es del: {porcentaje_descuento}%")

descuento_en_dinero = (porcentaje_descuento / 100) * precio_producto

precio_final = precio_producto - descuento_en_dinero
print(f"El precio final a pagar es de: ${precio_final} ARS")

dinero_ahorrado = precio_producto - precio_final
print(f"El dinero ahorrado es de: ${dinero_ahorrado} ARS")


# Ejercicio 9 - Tiempo de Vida
print("----- Ejercicio 9 -----")

edad_actual = 24
print(f"Tu edad actual es de: {edad_actual}")
 
dias_vividos = edad_actual * 365
print(f"Dias vividos aproximadamente: {dias_vividos}")

semanas_vividas = (4 * 12) * edad_actual
print(f"Semanas vividas aproximadamente: {semanas_vividas}")

años_para_llegar_80 = 80 - edad_actual
print(f"Para llegar a tener 80 años me faltan de vivir {años_para_llegar_80}")


# Ejercicio 10 - Análisis de Texto
print("----- Ejercicio 10 -----")

frase = "todo en la vida es temporal"

# frase con espacios
caracteres_de_frase = len(frase)
print(f"Caracteres de la frase: {caracteres_de_frase}")

# frase sin espacios (eliminando espacios)
caracteres_sin_espacios_frase = len(frase.replace(" ", ""))
print(f"Caracteres sin espacios en la frase: {caracteres_sin_espacios_frase}")

# contando las palabras
cantidad_palabras_frase = len(frase.split(" "))
print(f"Cantidad de palabras de la frase: {cantidad_palabras_frase}")


# Ejercicio 11 - Sistema de Puntuación
print("----- Ejercicio 11 -----")

puntos_nivel_1 = 100
puntos_nivel_2 = 250
puntos_nivel_3 = 500

# Cantidad de veces que un jugador completó el nivel 
cantidad_veces_completado_lvl_1 = 5
cantidad_veces_completado_lvl_2 = 3
cantidad_veces_completado_lvl_3 = 1

# calculando el puntaje total
puntaje_total = (puntos_nivel_1 * cantidad_veces_completado_lvl_1) + (puntos_nivel_2 * cantidad_veces_completado_lvl_2) + (puntos_nivel_3 * cantidad_veces_completado_lvl_3)
print(f"Puntaje total obtenido: {puntaje_total}")

# nivel promedio del jugador
suma_valores_niveles = (cantidad_veces_completado_lvl_1 * 1) + (cantidad_veces_completado_lvl_2 * 2) + (cantidad_veces_completado_lvl_3 * 3)

total_niveles_completados = cantidad_veces_completado_lvl_1 + cantidad_veces_completado_lvl_2 + cantidad_veces_completado_lvl_3

nivel_promedio = suma_valores_niveles / total_niveles_completados
print(f"El promedio de nivel del jugador es de: {nivel_promedio:.2f} aproximadamente.")


# Ejercicio 12 - Gestor de Presupuesto
print("----- Ejercicio 12 -----")

salario = 1500
alquiler = 350
comida_mensual = 750
gastos_vehiculo = 80
gastos_entretenimiento = 30

total_gastos = alquiler + comida_mensual + gastos_vehiculo + gastos_entretenimiento
print(f"El total de gastos fijos mensuales es de: {total_gastos} USD")

dinero_restante = salario - total_gastos
print(f"Por mes puedo ahorrar: {dinero_restante} USD")

porcentaje_gastos_sobre_salario = (total_gastos * 100) / salario
print(f"El porcentaje de gastos respecto a mi salario es de: {porcentaje_gastos_sobre_salario:.2f} %")

if porcentaje_gastos_sobre_salario > 80:
  print(f"Estas gastando mas del 80% de tu salario!")
else:
  print(f"No estas gastando mas del 80% de tu salario. Genial, puedes ahorrar dinero!")


# Ejercicio 13 - Conversión de Unidades
print("----- Ejercicio 13 -----")

tiempo_de_carrera_minutos = 1.48

carrera_en_segundos = tiempo_de_carrera_minutos * 60
print(f"El tiempo de carrera en segundos es de: {carrera_en_segundos:.2f}s")

carrera_en_horas = tiempo_de_carrera_minutos / 60
print(f"El tiempo de carrera en horas es de: {carrera_en_horas:.2f}h")


# Ejercicio 14 - Análisis de Ventas
print("----- Ejercicio 14 -----")

precio_unitario_producto_1 = 1200
precio_unitario_producto_2 = 800
precio_unitario_producto_3 = 210

cantidad_vendido_producto_1 = 15
cantidad_vendido_producto_2 = 23
cantidad_vendido_producto_3 = 12

ventas_producto_1 = cantidad_vendido_producto_1 * precio_unitario_producto_1
ventas_producto_2 = cantidad_vendido_producto_2 * precio_unitario_producto_2
ventas_producto_3 = cantidad_vendido_producto_3 * precio_unitario_producto_3

print(f"Ventas producto 1: ${ventas_producto_1}")
print(f"Ventas producto 2: ${ventas_producto_2}")
print(f"Ventas producto 3: ${ventas_producto_3}")

ventas_totales = ventas_producto_1 + ventas_producto_2 + ventas_producto_3
print(f"Ventas totales: ${ventas_totales}")

if cantidad_vendido_producto_1 > cantidad_vendido_producto_2 and cantidad_vendido_producto_1 > cantidad_vendido_producto_3:
  print(f"El producto mas vendido es el numero 1 con {cantidad_vendido_producto_1} ventas completadas")
elif cantidad_vendido_producto_2 > cantidad_vendido_producto_3:
  print(f"El producto mas vendido es el numero 2 con {cantidad_vendido_producto_2} ventas completadas")
else:
  print(f"El producto mas vendido es el numero 3 con {cantidad_vendido_producto_3} ventas completadas")  

numero_clientes = 50
ticket_promedio_por_cliente = ventas_totales / numero_clientes

print(f"El ticket promedio por cliente es de: ${ticket_promedio_por_cliente:.2f}")
  

# Ejercicio 15 - Sistema de Calificaciones
print("----- Ejercicio 15 -----")

peso_examen_1 = 20 / 100
peso_examen_2 = 25 / 100
peso_examen_3 = 30 / 100
peso_examen_4 = 25 / 100

# tabla de calificacion
# A: 90-100
# B: 80-89
# C: 70-79
# D: 60-69
# F: < 60
calificacion_examen_1 = 90 
calificacion_examen_2 = 90
calificacion_examen_3 = 80
calificacion_examen_4 = 85

promedio = (calificacion_examen_1 * peso_examen_1) + (calificacion_examen_2 * peso_examen_2) + (calificacion_examen_3 * peso_examen_3) + (calificacion_examen_4 * peso_examen_4)
print(f"Promedio ponderado: {promedio:.2f}")

if promedio >= 90 and promedio <= 100:
  print(f"Su calificación es A")
elif promedio >= 80 and promedio <= 89:
  print(f"Su calificacion es B")
elif promedio >= 70 and promedio <= 79:
  print(f"Su calificacion es C")
elif promedio >= 60 and promedio <= 69:
  print(f"Su calificacion es D")
elif promedio < 60:
  print(f"Su calificacion es F")  
else:
  print("Datos incorrectos!")
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

# Cantidad de veces que un jugador completó el nivel (puedes cambiar estos valores)
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
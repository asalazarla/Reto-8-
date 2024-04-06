import math

# Definir una función que toma x y calcula su arcotangente usando la serie de Maclaurin
def aproximar_arctan(x, terminos):
    suma = 0
    for i in range(terminos):
        termino = ((-1) ** i) * (x ** (2 * i + 1)) / (2 * i + 1)
        suma += termino
    return suma

# Determinar n para un error menor al 0.1%
error_objetivo = 0.001
x = float(input("Introduce el valor de x entre -1 y 1 para calcular arctan(x): "))

if x < -1 or x > 1:
    print("El valor de x está fuera del rango permitido.")
else:
    n_max = 100000  # Establecer un límite máximo para n por razones prácticas
    aproximacion = 0
    valor_real = math.atan(x)
    for n in range(1, n_max + 1):
        aproximacion_nueva = aproximar_arctan(x, n)
        error = abs(valor_real - aproximacion_nueva)
        if error < error_objetivo:
            aproximacion = aproximacion_nueva
            break

    if error < error_objetivo:
        print(f"Aproximación de arctan({x}) con {n} términos: {aproximacion}")
        print(f"Valor real de arctan({x}): {valor_real}")
        print(f"Número de términos necesarios para un error menor al 0.1%: {n}")
        print(f"Error: {error}")
    else:
        print("No se pudo alcanzar el error objetivo con el número máximo de términos establecido.")


#EJERCICIO 8
import math

# Función para aproximar e^x utilizando la serie de Taylor/Maclaurin
def aproximar_exponencial(x, n):
    aproximacion = 0
    # Iterar a través de cada término de la serie
    for i in range(n+1):  # Incluir el término n
        factorial = 1
        # Calcular el factorial de i sin usar math.factorial
        for j in range(1, i + 1):
            factorial *= j
        # Agregar el término actual a la suma de la aproximación
        aproximacion += (x ** i) / factorial
    return aproximacion

# Solicitar al usuario los valores de x y n
x = float(input("Introduce el valor de x: "))
n = int(input("Introduce el número de términos n: "))

# Calcular la aproximación y el valor real de e^x
aproximacion = aproximar_exponencial(x, n)
valor_real = math.exp(x)

# Mostrar la aproximación, el valor real y la diferencia entre ambos
print(f"Aproximación de e^{x} utilizando {n} términos: {aproximacion}")
print(f"Valor real de e^{x}: {valor_real}")
print


import math

def solicitar_entrada_flotante(mensaje):
    while True:
        entrada = input(mensaje)
        try:
            return float(entrada)
        except ValueError:
            print("La entrada no es un número válido. Por favor, intenta de nuevo.")

def solicitar_entrada_entera(mensaje):
    while True:
        entrada = input(mensaje)
        try:
            valor = int(entrada)
            if valor < 0:
                print("Por favor, introduce un número entero positivo.")
            else:
                return valor
        except ValueError:
            print("La entrada no es un número entero válido. Por favor, intenta de nuevo.")

# Ingresar el valor de x y el número de términos n utilizando las funciones de validación
x = solicitar_entrada_flotante("Introduce el valor de x (en radianes): ")
n = solicitar_entrada_entera("Introduce el número de términos n: ")

aproximacion = 0

# Calcular la aproximación de sen(x) utilizando la serie de Maclaurin
for i in range(n):
    # Calcular el factorial del denominador (2i+1)!
    factorial = 1
    for j in range(1, (2 * i) + 2):  # Calcular (2i+1)! sin usar math.factorial
        factorial *= j
    
    # Calcular el término i-ésimo de la serie
    termino = ((-1) ** i) * (x ** (2 * i + 1)) / factorial
    aproximacion += termino

# Calcular el valor real usando la función math.sin()
valor_real = math.sin(x)

# Mostrar la aproximación y la diferencia con el valor real
print(f"Aproximación de sen({x}) usando {n} términos: {aproximacion}")
print(f"Valor real de sen({x}): {valor_real}")
print(f"Diferencia: {abs(valor_real - aproximacion)}")


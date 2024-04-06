
# Se ingresa el número natural n
while True:
    try:
        n = int(input("Introduce un número natural n: "))
        if n >= 1:
            break  # Salir del bucle si el número es un entero positivo
        else:
            print("El número debe ser positivo y mayor que cero.")
    except ValueError:
        print("No has ingresado un número válido. Por favor, introduce un número natural.")

# Comprobar si el número ingresado es válido y proceder con el cálculo
if n >= 1:
    # Iterar sobre cada número hasta n para calcular su factorial
    for numero in range(1, n + 1):
        factorial = 1
        for i in range(2, numero + 1):  # Iniciar en 2, pues multiplicar por 1 no cambia el factorial
            factorial *= i
        # Imprimir el número y su factorial
        print(f"{numero}! = {factorial}")



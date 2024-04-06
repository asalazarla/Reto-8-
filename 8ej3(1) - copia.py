# Se ingresa un número natural n mayor o igual a 2
while True:
    try:
        n = int(input("Introduce un número natural n (n ≥ 2): "))
        if n >= 2:
            break
        else:
            print("El número debe ser mayor o igual a 2.")
    except ValueError:
        print("No has ingresado un número válido. Por favor, introduce un número natural.")

# Si n es impar, ajustarlo al par más cercano menor que n
if n % 2 != 0:
    n -= 1

# Imprimir los números pares en forma descendente hasta 2
for numero in range(n, 1, -2):
    print(numero)



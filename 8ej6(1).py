#EJERCICIO 6

try:
    # Se ingresa el número natural n y el número real x
    n = int(input("Introduce el exponente n (número natural): "))
    x = float(input("Introduce la base x (número real): "))

    # Inicializar el resultado a 1 (x^0)
    resultado = 1.0

    # Multiplicar resultado por x, n veces usando un ciclo for
    for _ in range(n):
        resultado *= x

    # Imprimir el resultado
    print(f"{x} elevado a la potencia de {n} es {resultado}")

except ValueError:
    print("Se esperaba que se introdujeran valores numéricos apropiados.")




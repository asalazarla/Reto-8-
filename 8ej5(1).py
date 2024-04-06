#EJERCICIO 5 
# Se ingresa el número n
entrada = input("Introduce el exponente n para calcular 2^n: ")
if entrada.isdigit():  # Comprobamos si la entrada es un dígito, lo cual implica un valor positivo
    n = int(entrada)
    # Inicializar el resultado a 1 (2^0)
    resultado = 1

    # Multiplicar resultado por 2, n veces
    for i in range(n):  # esto iterará n veces
        resultado *= 2

    # Imprimir el resultado
    print(f"2 elevado a la potencia de {n} es {resultado}")
else:
    print("No se ha ingresado un número entero válido.")



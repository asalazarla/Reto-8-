# Iterar a través de las tablas de multiplicar del 1 al 9
for numero in range(1, 10):
    print(f"Tabla de multiplicar del {numero}:")
    # Calcular cada producto de la tabla actual
    for multiplicador in range(1, 11):
        producto = numero * multiplicador
        print(f"{numero} x {multiplicador} = {producto}")
    # Espacio después de cada tabla para mejor legibilidad
    print("")



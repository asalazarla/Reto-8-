# Reto-8-

##**Este repo desarrolla los ejercicios propuestos en el reto ocho:).**

1.Imprimir un listado con los números del 1 al 100 cada uno con su respectivo cuadrado.
```python
# Imprimir los números del 1 al 100 y sus cuadrados
for numero in range(1, 101):  # El rango va de 1 a 100 incluido
    cuadrado = numero ** 2
    print(f"{numero} - {cuadrado}")
```



2.Imprimir un listado con los números impares desde 1 hasta 999 y seguidamente otro listado con los números pares desde 2 hasta 1000.
```python
# Imprimir los números impares desde 1 hasta 999
print("Números impares del 1 al 999:")
for numero in range(1, 1000, 2):  # El tercer argumento es el paso, que en este caso es 2
    print(numero)

# Imprimir los números pares desde 2 hasta 1000
print("\nNúmeros pares del 2 al 1000:")
for numero in range(2, 1001, 2):  # Iniciamos en 2 y vamos de dos en dos hasta 1000
    print(numero)
```



3.Imprimir los números pares en forma descendente hasta 2 que son menores o iguales a un número natural n ≥ 2 dado
```python
    # Suponiendo que n es el número natural dado y es mayor o igual a 2
n = int(input("Introduce un número natural n (n ≥ 2): "))

# Comprobamos que n es mayor o igual a 2
if n < 2:
    print("El número debe ser mayor o igual a 2.")
else:
    # Imprimir los números pares en forma descendente hasta 2
    for numero in range(n, 1, -2):
        if numero % 2 != 0:  # Si el número es impar, restamos 1 para hacerlo par
            numero -= 1
        print(numero)
```



4.Imprimir los números de 1 hasta un número natural n dado, cada uno con su respectivo factorial
```python
# Se ingresa el número natural n
n = int(input("Introduce un número natural n: "))

# Comprobar si el número ingresado es válido
if n < 1:
    print("El número debe ser positivo.")
else:
    # Iterar sobre cada número hasta n para calcular su factorial
    for numero in range(1, n + 1):
        factorial = 1
        # Calcular el factorial del número actual
        for i in range(1, numero + 1):
            factorial *= i
        # Imprimir el número y su factorial
        print(f"{numero}! = {factorial}")
```


5.Calcular el valor de 2 elevado a la potencia n usando ciclos for.
```python
# Se ingresa el número n
n = int(input("Introduce el exponente n para calcular 2^n: "))

# Inicializar el resultado a 1 (2^0)
resultado = 1

# Multiplicar resultado por 2, n veces
for i in range(n):  # esto iterará n veces
    resultado *= 2

# Imprimir el resultado
print(f"2 elevado a la potencia de {n} es {resultado}")
```

6.Leer un número natural n, leer otro dato de tipo real x y calcular x^n usando ciclos for. Disclaimer: Trate de no utilizar el operador de potencia (**).
```python
# Se ingresa el número natural n y el número real x
n = int(input("Introduce el exponente n (número natural): "))
x = float(input("Introduce la base x (número real): "))

# Inicializar el resultado a 1 (x^0)
resultado = 1.0

# Multiplicar resultado por x, n veces
for _ in range(n):  # El guión bajo es una variable no utilizada.
    resultado *= x

# Imprimir el resultado
print(f"{x} elevado a la potencia de {n} es {resultado}")
```


7.Diseñe un programa que muestre las tablas de multiplicar del 1 al 9.
```python
# Iterar a través de las tablas de multiplicar del 1 al 9
for numero in range(1, 10):
    print(f"Tabla de multiplicar del {numero}:")
    # Calcular cada producto de la tabla actual
    for multiplicador in range(1, 11):
        producto = numero * multiplicador
        print(f"{numero} x {multiplicador} = {producto}")
    # Espacio después de cada tabla para mejor legibilidad
    print("")
```


8.Diseñar una función que permita calcular una aproximación de la función exponencial alrededor de 0 para cualquier valor x (real), utilizando los primeros n términos de la serie de Maclaurin. Nota: use math para traer la función exponencial y mostrar la diferencia entre el valor real y la aproximación.

[![Captura-de-pantalla-2024-04-05-224629.png](https://i.postimg.cc/Wpg5L3SX/Captura-de-pantalla-2024-04-05-224629.png)](https://postimg.cc/pyVfKPwF)

```python
import math

def aproximar_exponencial(x, n):
    aproximacion = 0
    for i in range(n+1):  # Asegurándonos de incluir el término n
        factorial = 1
        for j in range(1, i + 1):  # Calcular i! sin usar math.factorial
            factorial *= j
        aproximacion += (x ** i) / factorial  # Sumamos el término a la aproximación
    return aproximacion

# Ingresar el valor de x y el número de términos n
x = float(input("Introduce el valor de x: "))
n = int(input("Introduce el número de términos n: "))

# Calcular la aproximación y el valor real
aproximacion = aproximar_exponencial(x, n)
valor_real = math.exp(x)

# Mostrar resultados y la diferencia
print(f"Aproximación de e^{x} utilizando {n} términos: {aproximacion}")
print(f"Valor real de e^{x}: {valor_real}")
print(f"Diferencia: {abs(valor_real - aproximacion)}")
```


9. Diseñar una función que permita calcular una aproximación de la función seno alrededor de 0 para cualquier valor x (real), utilizando los primeros n términos de la serie de Maclaurin. Nota: use math para traer la función seno y mostrar la diferencia entre el valor real y la aproximación.

[![Captura-de-pantalla-2024-04-05-224835.png](https://i.postimg.cc/prJQ9m6v/Captura-de-pantalla-2024-04-05-224835.png)](https://postimg.cc/4HnHqxG2)

```python
import math

# Ingresar el valor de x y el número de términos n
x = float(input("Introduce el valor de x (en radianes): "))
n = int(input("Introduce el número de términos n: "))

aproximacion = 0

# Calcular la aproximación de sen(x) utilizando la serie de Maclaurin
for i in range(n):
    # Calcular el factorial del denominador (2i+1)!
    factorial = 1
    for j in range(1, (2 * i) + 2):
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
```



10. Diseñar una función que permita calcular una aproximación de la función arcotangente alrededor de 0 para cualquier valor x en el rango [-1, 1], utilizando los primeros n términos de la serie de Maclaurin. Nota: use math para traer la función arctan y mostrar la diferencia entre el valor real y la aproximación.

[![Captura-de-pantalla-2024-04-05-224923.png](https://i.postimg.cc/Hxrjh2ZB/Captura-de-pantalla-2024-04-05-224923.png)](https://postimg.cc/CBVFZjVq)

```python
import math

# Definir una función que toma x y calcula su arcotangente usando la serie de Maclaurin
def aproximar_arctan(x, terminos):
    suma = 0
    # Usar un ciclo for con un rango para calcular los términos de la serie
    for i in range(terminos):
        # Calcular el término i-ésimo de la serie
        termino = ((-1) ** i) * (x ** (2 * i + 1)) / (2 * i + 1)
        suma += termino
    return suma

# Determinar n para un error menor al 0.1%
error_objetivo = 0.001
n = 0
x = float(input("Introduce el valor de x entre -1 y 1 para calcular arctan(x): "))

# Asegurar que x está en el rango permitido
if x < -1 or x > 1:
    print("El valor de x está fuera del rango permitido.")
else:
    # Calcular la aproximación y comparamos con el valor real hasta alcanzar el error deseado
    while True:
        aproximacion = aproximar_arctan(x, n)
        valor_real = math.atan(x)
        error = abs(valor_real - aproximacion)
        if error < error_objetivo:
            break
        n += 1

    # Se muestran los resultados
    print(f"Aproximación de arctan({x}) con {n} términos: {aproximacion}")
    print(f"Valor real de arctan({x}): {valor_real}")
    print(f"Número de términos necesarios para un error menor al 0.1%: {n}")
    print(f"Error: {error}")
```
        

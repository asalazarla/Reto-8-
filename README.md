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
```



4.Imprimir los números de 1 hasta un número natural n dado, cada uno con su respectivo factorial
```python
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
```


5.Calcular el valor de 2 elevado a la potencia n usando ciclos for.
```python
# Inicializar la variable 'n' fuera del bucle
n = None

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
```

6.Leer un número natural n, leer otro dato de tipo real x y calcular x^n usando ciclos for. Disclaimer: Trate de no utilizar el operador de potencia (**).
```python
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

```


9. Diseñar una función que permita calcular una aproximación de la función seno alrededor de 0 para cualquier valor x (real), utilizando los primeros n términos de la serie de Maclaurin. Nota: use math para traer la función seno y mostrar la diferencia entre el valor real y la aproximación.

[![Captura-de-pantalla-2024-04-05-224835.png](https://i.postimg.cc/prJQ9m6v/Captura-de-pantalla-2024-04-05-224835.png)](https://postimg.cc/4HnHqxG2)

```python
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
```



10. Diseñar una función que permita calcular una aproximación de la función arcotangente alrededor de 0 para cualquier valor x en el rango [-1, 1], utilizando los primeros n términos de la serie de Maclaurin. Nota: use math para traer la función arctan y mostrar la diferencia entre el valor real y la aproximación.

[![Captura-de-pantalla-2024-04-05-224923.png](https://i.postimg.cc/Hxrjh2ZB/Captura-de-pantalla-2024-04-05-224923.png)](https://postimg.cc/CBVFZjVq)

```python
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

```
        

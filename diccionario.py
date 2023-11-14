from itertools import product

# Wordlist de nombres de colores
colores = ["rojo", "verde", "azul", "amarillo"]

# Wordlist de números
numeros = ["uno", "dos", "tres", "cuatro"]

# Crear el wordlist combinando los dos
combinaciones = list(product(colores, numeros))

# Imprimir el wordlist resultante
for combinacion in combinaciones:
    print(''.join(combinacion))

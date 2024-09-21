def factorial(n):
    # Verificamos que n sea un número entero no negativo
    if n < 0:
        return "El factorial no está definido para números negativos."
    resultado = 1  # Inicio con 1 porque es el elemento neutro para la multiplicación
    for i in range(1, n + 1):  # Recorremos desde 1 hasta n
        resultado *= i  # Multiplicamos el resultado por cada número
    return resultado  # Retornamos el resultado final

# Ejemplos de uso
print(factorial(5))  # Imprime: 120
print(factorial(0))  # Imprime: 1
print(factorial(-3))  # Imprime: El factorial no está definido para números negativos.
print(factorial(10))  # Imprime: 3628800
print(factorial(15))  # Imprime: 1307674368000
print(factorial(20))  # Imprime: 2432902008176640000
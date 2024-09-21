def fibonacci(n):
    # Inicializamos la lista con los primeros dos números de la serie
    fib_sequence = [0, 1]
    
    # Verificamos si n es menor o igual a 0, en cuyo caso devolvemos una lista vacía
    if n <= 0:
        return []
    # Si n es 1, devolvemos solo el primer número de la serie
    elif n == 1:
        return [0]
    
    # Generamos la serie hasta n
    while True:
        next_fib = fib_sequence[-1] + fib_sequence[-2]  # Sumar los últimos dos números
        if next_fib > n:  # Verificamos si el siguiente número excede el límite
            break
        fib_sequence.append(next_fib)  # Agregamos el nuevo número a la secuencia
    
    return fib_sequence  # Devolvemos la secuencia generada

# Ejemplo de uso
limite = 21
resultado = fibonacci(limite)
print(f"La serie de Fibonacci hasta {limite} es: {resultado}")

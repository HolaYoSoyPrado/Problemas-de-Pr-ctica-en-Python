#Suma de numeros pares
def suma_pares(lista_numeros):
    suma = 0  # Inicializamos la suma en 0

    # Recorremos cada número en la lista
    for numero in lista_numeros:
        if numero % 2 == 0:  # Verificamos si el número es par
            suma += numero  # Sumamos el número par a la suma total

    return suma  # Devolvemos la suma total de los números pares

numeros = [1, 2, 3, 4, 5, 6]
resultado = suma_pares(numeros)
print(resultado)  # Esto imprimirá 12, que es 2 + 4 + 6


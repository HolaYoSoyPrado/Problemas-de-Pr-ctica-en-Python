def convertir_temperatura(valor, unidad):
    """
    Convierte una temperatura entre Celsius y Fahrenheit.
    
    :param valor: La temperatura a convertir.
    :param unidad: La unidad de la temperatura a convertir ('C' para Celsius, 'F' para Fahrenheit).
    :return: La temperatura convertida.
    """
    
    if unidad.upper() == 'C':  # Verifica si la unidad es Celsius
        # Convierte de Celsius a Fahrenheit
        fahrenheit = valor * (9 / 5) + 32
        return fahrenheit
    elif unidad.upper() == 'F':  # Verifica si la unidad es Fahrenheit
        # Convierte de Fahrenheit a Celsius
        celsius = (valor - 32) * (5 / 9)
        return celsius
    else:
        return "Unidad no válida. Usa 'C' para Celsius o 'F' para Fahrenheit."

# Ejemplos de uso
temperatura_c = 25
temperatura_f = 77

print(f"{temperatura_c} °C son {convertir_temperatura(temperatura_c, 'C')} °F")
print(f"{temperatura_f} °F son {convertir_temperatura(temperatura_f, 'F')} °C")

def convertir_a_fahrenheit():
    
    celsius = float(input("Inserte una temperatura en celsius: "))
    farenheit = (celsius * 9 / 5 + 32)

    return celsius, farenheit

def main():

    conversion = convertir_a_fahrenheit()
    print(conversion)


    
if __name__ == "__main__":
    main()


# - ej04 => NO recibe parámetros y retorna una cadena de caracteres con la temperatura convertida en grados Celsius y entre parántesis la temperatura en grados farenheit... ambas temperaturas con 2 posiciones decimales. Por ejemplo, si introduce 212 debe retornar la cadena "100.00ºC (212.00ºF)". Dentro de la función se pedirá al usuario los grados Farenheit.
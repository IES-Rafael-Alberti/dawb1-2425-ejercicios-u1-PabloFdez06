def convertir_a_fahrenheit(celsius):
    
    farenheit = (celsius * 9 / 5 + 32)

    return farenheit

def main():

    celsius = float(input("Inserte una temperatura en celsius: "))

    conversion = convertir_a_fahrenheit(celsius)
    print(f"{celsius:.2f}ºC, {conversion:.2f}ºF")


    
if __name__ == "__main__":
    main()

# La función `grados_celsius(farenheit: float) -> float` recibe los grados farenheit (redondeados a dos posiciones decimales) y retorna los grados celsius (redondeados a dos posiciones).
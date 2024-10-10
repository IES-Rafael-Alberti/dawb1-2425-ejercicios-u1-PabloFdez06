
def comprobarnum(cadena):
    cadena = cadena.strip()
    return cadena.isdigit() or (cadena.startswith("-") and cadena[1:].isdigit())


def damenumero():
    cadena = input("Introduce un numero entero: ")

    while not comprobarnum(cadena): 
        cadena = input("El número que has introducido no es entero\n Introduce un numero entero: ")

    return int(cadena)


def main():
    num = damenumero()
    print(f"Has introducido el número {num}")

if __name__ == "__main__":
    main()
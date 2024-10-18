# SI HAY ERROR FINALIZA EL PROGRAMA Y TE ECHA:

# def comprobar_numero(entrada: str) -> bool:
#     try:
#         float(entrada)
#     except ValueError:
#         print("Número no válido!")
#         return False
#     return True

    
# def main():
#     entrada = input("Introduce un número: ")
#     if comprobar_numero(entrada) == True:
#         print(f"{float(entrada)}")    


# if __name__ == "__main__":
#     main()

# SI EL NUMERO FALLA VUELVE A PEDIRTELO HASTA QUE EL FORMATO INTRODUCIDO SEA CORRECTO.

def introducir_numero(msj: str) -> bool:
    num = None

    try:
        num = float(input(msj))
    except ValueError:
        print("Número inválido")

    return num

    
def main():

    num = introducir_numero("Introduce un número: ")
    while (num is None):
        num = introducir_numero("Introduce un número: ")


if __name__ == "__main__":
    main()
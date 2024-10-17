def comprobar_numero(valor: str):

    if valor.startswith("-"):
        valor = valor[1:]

    return valor.isdigit()

def introducir_numero(msj: str):
    valor = input(msj).strip().lower
    
    if comprobar_numero(valor):
        return True, int(valor)
    else:
        if valor == "fin":
            return False, None
        else:
            return False, None

def main(): 
    contador = 0
    suma = 0
    media = 0

    encuentra_fin = False

    while not encuentra_fin:
        entrada_ok, numero = introducir_numero("Introduzca un número: ")
        if entrada_ok and numero is not None:
            contador += 1
            suma += numero
        elif entrada_ok and numero is None:
            encuentra_fin = True
        else:
            print("Entrada Inválida!")

    if contador > 0:
        media = suma / contador

    print(f"{suma}, {contador}, {media}")


if __name__ == "__main__":
    main()
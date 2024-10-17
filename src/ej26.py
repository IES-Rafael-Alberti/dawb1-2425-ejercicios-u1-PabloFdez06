def separa_lista(productos: str):
    separar_intro = productos.split("\n")

    return separar_intro

def main():
   
    lista = input("Introduce la lista de la compra separada por comas: ")
    separar_intro = separa_lista(lista)
    
    print(separar_intro)


if __name__ == "__main__":
    main()


# Escribir un programa que pregunte por consola por los productos de una cesta de la compra, separados por comas, y muestre por pantalla cada uno de los productos en una línea distinta.

#### PREGUNTAR EN CLASE ####
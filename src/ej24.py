def precio_producto():
    precio = str(input("Introduce el precio del producto en € y con 2 decimales: "))
    
    precio_dividido = precio.split(".")
    euro = precio_dividido
    
    print("El precio es de ", euro, "euros")

def main():
    precio_producto()

if __name__ == "__main__":
    main()


# el número de euros y el número de céntimos del precio introducido.
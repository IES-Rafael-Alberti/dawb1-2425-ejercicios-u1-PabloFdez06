def precio_producto():
    precio = float(input("Introduce el precio del producto en € y con 2 decimales: "))
    
    # precio_dividido = precio.split(".")
    # euro = precio_dividido[0]
    # centimos = precio_dividido[1]

    
    
    # print("El precio es " + euro + " euros" + " Y " + centimos + " centimos.")

    print("El precio es de {:.d} y {:.2f}".format(precio))

def main():
    precio_producto()

if __name__ == "__main__":
    main()


# el número de euros y el número de céntimos del precio introducido.
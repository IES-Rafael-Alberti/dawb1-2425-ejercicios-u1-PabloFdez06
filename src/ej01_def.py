
def recibe_nombre():
    nombre = input("Escribe tu nombre: ")
    return str(nombre)

def main():
    nombre = recibe_nombre()
    print(f"Tu nombre es: {nombre}")

    
if __name__ == "__main__":
    main()
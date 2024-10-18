
def recibe_nombre(nombre):
    return str(nombre)

def main():
    
    nombre = input("Escribe tu nombre: ")
    nombre = recibe_nombre(nombre)
    
    print(f"Tu nombre es: {nombre}")

    
if __name__ == "__main__":
    main()
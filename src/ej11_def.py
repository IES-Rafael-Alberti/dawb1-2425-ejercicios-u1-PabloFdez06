# ej11 => recibe un número y retorna una cadena de caracteres con el resultado de la función.

def recibe_num(num):
    suma = num*(num + 1) / 2
    return suma


def main():
    
    num = int(input("Introduce un número entero positivo: "))    
    suma = recibe_num(num)
    print("Resultado de la formula: " + str(suma))

  

if __name__ == "__main__":
    main()

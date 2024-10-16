




# ej11 => recibe un número y retorna una cadena de caracteres con el resultado de la función.

def recibe_num(num):
    suma = num*(num + 1) / 2
    return print("Resultado de la formula: " + str(suma))



def main():
    
    num = int(input("Introduce un número entero positivo: "))
    num = recibe_num(num)
    


if __name__ == "__main__":
    main()

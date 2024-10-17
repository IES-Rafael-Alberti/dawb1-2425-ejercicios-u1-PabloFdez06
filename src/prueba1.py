def retornar_numero(num1, num2):
    if num1 == num2:
        return 0
    elif num1 < num2:
        return num2
    else:
        return num1
    
def main():
    num1 = input("Introduce el primer número: ")
    num2 = input("Introduce el otro número: ")

    resultado = retornar_numero(num1, num2)

    print("El número mayor es: ", resultado)

if __name__ == "__main__":
    main()
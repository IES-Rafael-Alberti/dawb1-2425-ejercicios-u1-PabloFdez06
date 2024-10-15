## Ejercicio 1.28 *(ej28.py)*

# Realiza un programa en Python que lea dos números enteros, muestre cuál es el menor de los dos y cuántos números existen entre ellos dos.

#   - El segundo número no puede ser igual, si es así, debe mostrar el error: **"Los números no pueden ser iguales"**.
#   - Si los números son diferentes, por ejemplo, 5 y 12, debe mostrar la frase: **"El número menor es el 5 y entre ellos existen 7 números enteros"**.

def pedir_num():
    num1 = int(input("Inserte el primer número: "))
    num2 = int(input("Inserte el segundo número: "))

    return num1, num2

def comprobar_num(num1, num2):

    if num1 == num2:
        return "Los números no pueden ser iguales"
    
    elif num1 > num2:
        return f"El número menor es {num2} y entre ellos existen {(num1 - num2) - 1} números enteros"
    
    else:
        return f"{num1} es menor que {num2} y hay {(num2 - num1) -1} números de diferencia"
     


def main():
    num1, num2 = pedir_num()
    resultado = comprobar_num(num1, num2)
    print(resultado)


if __name__ == "__main__":
    main()
## Ejercicio 1.29 *(ej29.py)*

# Realiza un programa en Python que solicite un nombre y una edad.

#   - Si el nombre está vacío, debes utilizar el valor **"Desconocido"**. La edad debe pedirse hasta que introduzca una edad comprendida entre 0 y 125 años.
#   - El programa mostrará la siguiente frase: **"Te llamas Pepito y tienes 20 años, te quedan aún 105 años por cumplir"**.


def comprobar_nombre(nombre):
    if nombre.strip() == "":
        return "**Desconocido**"
        
    else:
        return nombre


def comprobar_edad():

    edad = input("Introduce una edad: ")

    while not edad.isdigit() or not (0 <= int(edad) <= 125):
        print("Debes introducir un valor de entre 0 y 125 años")
        edad = input("Introduce una edad: ")

    return int(edad)
    

def main():

    nombre = input("Introduce un nombre: ")
    nombre = comprobar_nombre(nombre)

    edad = comprobar_edad()

    print(f"Te llamas {nombre} y tienes {edad} años, te quedan aún {125 - edad} años por cumplir.")



if __name__ == "__main__":
    main()


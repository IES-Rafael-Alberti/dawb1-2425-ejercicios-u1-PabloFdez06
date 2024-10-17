def introduce_fecha(fecha_nacimiento):

    fecha_nacimiento = fecha_nacimiento.strip()

    dia, mes, año = fecha_nacimiento.split("/")

    dia = int(dia)
    mes = int(mes)


    return dia, mes, año

def main():
    
    fecha_nacimiento = input("Introduce tu fecha de nacimiento con el siguiente formato **dd/mm/aaaa**: ")
    dia, mes, año = introduce_fecha(fecha_nacimiento)
    
    print(f"Dia: {dia}, Mes: {mes}, Año: {año}")


if __name__ == "__main__":
    main()
    


# Escribir un programa que pregunte al usuario la fecha de su nacimiento en formato dd/mm/aaaa y muestra por pantalla, el día, el mes y el año. Adaptar el programa anterior para que también funcione cuando el día o el mes se introduzcan con un solo carácter.


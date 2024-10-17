# horas = int(input("Horas de trabajo: "))
# precio = int(input("Coste por hora: "))
# total = str(horas * precio)

# print("Importe total: " + total)

def recibe_horasycoste():
    horas = int(input("Horas de trabajo: "))
    precio = int(input("Coste por hora: "))

    return (horas * precio)


def main():
    importe = recibe_horasycoste()
    print(f"El importe total es: {importe}")


if __name__ == "__main__":
    main()


# ej02 => recibe horas y coste y retorna el importe total.

def correo_dominios():
    correo_personal = input("Introduce tu correo electronico: ")
    arroba = correo_personal.find("@")

    correo_deu = correo_personal[0:arroba + 1] + "ceu.es"
    print(correo_deu)


def main():
    correo_dominios()

if __name__ == "__main__":
    main()


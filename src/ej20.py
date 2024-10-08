def dame_telefono(numero):
    """ print(numero[4:13]) """
    """ print(numero.split("-")[1]) """
    pos1 = numero.find("-") + 1
    pos2 = numero.find("-", pos1)
    return numero[pos1:pos2]



def main():
    numero = input("Introduce tu número de telefono: ") # +34-913724710-56
    print(dame_telefono(numero))

if __name__ == "__main__":
    main()
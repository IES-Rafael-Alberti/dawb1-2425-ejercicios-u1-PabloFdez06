def frase_vocal():
    frase = input("Introduce la frase: ")
    vocal = input("Introduce la vocal: ")

    vocal = vocal.upper()
    print(frase + vocal)

def main():
    frase_vocal()

if __name__ == "__main__":
    main()

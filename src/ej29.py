import random

def generar_num_aleatorio():
    return random.randint(1, 100)

def main():
    print (f"El numero aleatorio es: {generar_num_aleatorio()}")

if __name__ == "__main__":
    main()
# # Mostrar todos los divisores de un número

# def division_retorna_resultado(numero_a_dividir):
#     for numero_a_dividir in range (numero_a_dividir, 1):
#         if numero_a_dividir == 0:
#             return "3"




# def main():
#     numero_a_dividir = input("Introduce el número a sacar sus divisores: ")
#     numero_a_dividir = division_retorna_resultado(numero_a_dividir)


# if __name__ == "__main__":
#     main()

# Mostrar todos los divisores de un número

def division_retorna_resultado(num: int) -> str:
    # 1, 2, 5, 11
    

    if num <= 1:
        divisores = "1"
    else:
        divisores = "1, "

        for i in range(2, num):
            if num % i == 0:
                divisores += f"{i}, "
        
        divisores += f"{num}"

    return divisores    
    




def main():

    num = int(input("Introduce el numero del que quieres obtener sus divisores: "))
    print(f"Los divisores de {num} son: {division_retorna_resultado(num)}.")


if __name__ == "__main__":
    main()
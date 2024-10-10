import math

def calculararea(a: float, b: float, c: float) -> float:
    semiper = (a + b + c) / 2
    area = math.sqrt(semiper * (semiper - a) * (semiper - b) * (semiper - c))

    return area

def comprobar_float(valor: str) -> bool:
    if valor.startswith("-"): # "-88.67"
        valor = valor[1:] # "88.67"

    pos_punto = valor.find(".") # 2
    if pos_punto >= 0: 
        valor = valor[:pos_punto] + valor[pos_punto + 1: ] # "8867"

    return valor.isdigit()

def comprobar_angulos(a, b, c):
    return (a + b > c) and (a + c > b) and (b + c > a)



def intruduce_numero(msj: str) -> float:
    valor = input(msj).strip().replace(",", ".")


    while comprobar_float(valor) == False:
        print("\n***ERROR*** Número invalido!")
        valor = input(msj).strip().replace(",", ".")

    return float(valor)



def main():
    print("Dame los 3 lados del triángulo...")
    
    lado_a = intruduce_numero("Introduce el lado 1: ")
    lado_b = intruduce_numero("Introduce el lado 2: ")
    lado_c = intruduce_numero("Introduce el lado 3: ")

    if comprobar_angulos(lado_a, lado_b, lado_c):
        area = calculararea(lado_a, lado_b, lado_c)
        print(f"El área del triángulo con los lados ({lado_a:.2f} {lado_b:.2f} {lado_c:.2f}) es {area:.2f}.")

    else:
        print(f"No se puede calcular el area con los siguientes lados: ({lado_a:.2f} {lado_b:.2f} {lado_c:.2f}).")



    
if __name__ == "__main__":
    main()
# * *ej05_**def2**.py* => La función `calcula_precio(importe: float, iva: float) -> str` recibe el importe y el iva, si el iva está fuera del rango 0-100 se aplicará el 21%, y retornará una cadena de caracteres con el iva y el precio con iva mostrando solo 2 posiciones decimales. Ejemplo: calcula_precio(100, 21) -> "El precio final del artículo con IVA (21.00) es 121.00€."


def precio_iva(porcentaje, importe):

    if not (0 < porcentaje <= 100):
        porcentaje = 21

    porcentaje = porcentaje / 100
    iva = importe * porcentaje
    resultado = iva + importe

    return resultado

    



def main():

    
    porcentaje = float(input(f"Indique el porcentaje de IVA a añadir: "))
    importe = float(input("Especifique el importe sin iVA: "))
    precio_iva(porcentaje, importe)

    resultado = precio_iva(porcentaje, importe)
    
    print(f"El precio final del articulo con IVA es de: {resultado:.2f}")



if __name__ == "__main__":
    main()





# ej05 => recibe el importe del artículo sin iva y el tipo de iva a aplicar, pero no retorna nada, sino que se imprime desde dentro de la función.
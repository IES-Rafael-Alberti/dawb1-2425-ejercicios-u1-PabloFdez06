
def precio_iva(importe, porcentaje):

    iva = importe * porcentaje
    resultado = iva + importe
    print (f"El precio final del articulo con IVA es de: {resultado:.2f}") # formato IVA x.xx

def main():

    importe = float(input("Especifique el importe sin iVA: "))
    porcentaje = float(input("Indique el porcentaje de IVA a añadir: "))
    precio_iva(importe, porcentaje)



    
if __name__ == "__main__":
    main()


# ej05 => recibe el importe del artículo sin iva y el tipo de iva a aplicar, pero no retorna nada, sino que se imprime desde dentro de la función.
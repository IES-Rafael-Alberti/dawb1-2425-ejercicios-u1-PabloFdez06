importe = float(input("Especifique el importe sin iVA: "))
porcentaje = float(input("Indique el porcentaje de IVA a añadir: "))
iva = importe * porcentaje

print("El precio final del articulo con IVA es de: " + str(importe + iva))

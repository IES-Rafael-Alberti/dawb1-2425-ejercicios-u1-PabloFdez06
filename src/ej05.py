importe = float(input("Especifique el importe sin iVA: "))
porcentaje = float(input("Indique el porcentaje de IVA a añadir: "))
iva = importe * porcentaje
resultado = iva + importe

print (f"El precio final del articulo con IVA es de: {resultado:.2f}")

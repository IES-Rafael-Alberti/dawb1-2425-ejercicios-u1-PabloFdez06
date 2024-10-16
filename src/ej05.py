importe = float(input("Especifique el importe sin iVA: "))
porcentaje = float(input("Indique el porcentaje de IVA a añadir: "))
iva = importe * porcentaje
resultado = iva + importe

print (f"El precio final del articulo con IVA es de: {resultado:.2f}")

# ej05 => recibe el importe del artículo sin iva y el tipo de iva a aplicar, pero no retorna nada, sino que se imprime desde dentro de la función.
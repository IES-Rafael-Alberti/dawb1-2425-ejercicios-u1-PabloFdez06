precioiva = float(input("Indica el precio final del objeto con IVA: "))
preciosiniva = precioiva / 1.10
ivapagado = precioiva - preciosiniva

print("El importe de IVA pagado es de: " + str(ivapagado) + "€")
print("El importe sin IVA es de: " + str(preciosiniva) + "€")

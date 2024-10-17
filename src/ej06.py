precioiva = float(input("Indica el precio final del objeto con IVA: "))
preciosiniva = precioiva / 1.10
ivapagado = precioiva - preciosiniva

print(f"El importe de IVA pagado es de: {ivapagado:.2f}€")
print(f"El importe sin IVA es de: {preciosiniva:.2f}€")

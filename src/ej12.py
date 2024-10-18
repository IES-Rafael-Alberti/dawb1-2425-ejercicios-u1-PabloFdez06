peso = float(input("Inserta tu peso corporal en kilogramos: "))
medida = float(input("Ingrese su medida en metros: "))

indicemasa = peso / medida

print("Tu índice de masa corporal es donde es el índice de masa corporal calculado redondeado con dos decimales. " + str(round(indicemasa, 2)))
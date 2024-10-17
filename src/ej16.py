PRECIOPAN = 3.49

PANAYER = float(input("Cuantas barras de pan de ayer se han vendido hoy? "))
PRECIODESCUENTO = PANAYER * (3.49 * 0.4)

print(f"El precio habitual de una barra de pan es: {PRECIOPAN}€.\nEl descuento que se le realiza a una barra por no ser fresca es del 60%.\nY el precio final de las barras con descuento es de {PRECIODESCUENTO:.2}€")
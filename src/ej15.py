capital = float(input("Intruduce la cantidad que se haya en tu cuenta de ahorros: "))
interes = float(0.04)

capital1 = capital + capital * interes
capital2 = capital1 + capital * interes
capital3 = capital2 + capital * interes

print("Tus ahorros del primer año son ", capital1, "Los del segundo año son", capital2, "y los del tercer año son", capital3,".")

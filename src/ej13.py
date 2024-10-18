n = int(input("Introduzca 1 número entero: "))
m = int(input("Introduzca el segundo número entero: "))

c = int(n / m)
r = n % m

print("la división de", n, "entre", m, "da un cociente", c, "y un resto", r, "donde", n, "y", m, "son los números introducidos por el usuario, y", c, "y", r, "son el cociente y el resto de la división entera respectivamente")
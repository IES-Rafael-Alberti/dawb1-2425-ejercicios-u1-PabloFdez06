import random

def generar_num_aleatorio():
    return random.randint(1, 100)

def pista_segun_cercania(numero_aleatorio, intento):
    
    diferencia = abs(numero_aleatorio - intento) # abs devuelve el valor absoluto del numero 

    if diferencia == 0: 
            return "Felicidades! Has adivinado el número"
   
    elif diferencia <= 4:
         return "Tas que arde shurra"
    
    elif diferencia <= 10:
         return "Calentito calentito!"
    
    elif diferencia <=15:
        return "Templaito"
    
    elif diferencia <=30:
        return "Fresquito polo fla"
    
    else: 
         return "Más frio que en la comunión del pingu"
    

def main(): 
    print("\nEsto es un juego para adivinar un número aleatorio, Bienvenido! \n")
    numero_aleatorio = generar_num_aleatorio()

    numero_intentos = 3

    while numero_intentos > 0:
         print(f"Tienes {numero_intentos} intentos restantes...")

         intento = int(input("Adivina el número situado entre 1 y 100: "))

         if intento < 1 or intento > 100:
              print("Asegurese de introducir un número entre el 1 y el 100 porfavor.")

         pista = pista_segun_cercania(numero_aleatorio, intento)
         print(pista)

         if pista == "Felicidades! Has adivinado el número":
              break
         
         numero_intentos -= 1

    if numero_intentos == 0:
         print(f"Lo siento, no te quedan más intentos, el número era {numero_aleatorio}")



if __name__ == "__main__":
    main()


# El juego consta de recibir un numero aleatorio que no se muestre en pantalla, y el usuario debe tratar de adivinarlo, si dice un número cercano a el, debe darle una pista como "caliente si esta cerca, frio si aun esta lejos, y si está muy cerca decir como ardiendo, en caso de estar muy lejos, congelao" Solo tendrás 3 intentos

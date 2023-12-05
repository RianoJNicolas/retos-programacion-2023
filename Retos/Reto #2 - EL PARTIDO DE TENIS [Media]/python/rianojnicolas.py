"""
Escribe un programa que muestre cómo transcurre un juego de tenis y quién lo ha ganado.
El programa recibirá una secuencia formada por "P1" (Player 1) o "P2" (Player 2), según quien
gane cada punto del juego.

- Las puntuaciones de un juego son "Love" (cero), 15, 30, 40, "Deuce" (empate), ventaja.
- Ante la secuencia [P1, P1, P2, P2, P1, P2, P1, P1], el programa mostraría lo siguiente:
  15 - Love
  30 - Love
  30 - 15
  30 - 30
  40 - 30
  Deuce
  Ventaja P1
  Ha ganado el P1
- Si quieres, puedes controlar errores en la entrada de datos.   
- Consulta las reglas del juego si tienes dudas sobre el sistema de puntos.   
"""

def input_match():
    match = input("ingresa la secuencia del juego: ").upper()
    list_match = match.split(",")
    # trim a los elementos de la lista
    list_match = [i.strip() for i in list_match]

    # verificacion de los elementos de la lista
    for i in list_match:
        if i != "P1" and i != "P2":
            print("Error: La secuencia solo puede contener P1 o P2")
            exit()
    return list_match


points = {0: "Love", 1: "15", 2: "30", 3: "40"}

# funcion para llevar el conteo de los puntos, input es una secuencia de P1 y P2
def score(match):
    # variables para llevar el conteo de los puntos
    p1 = 0
    p2 = 0
    # ciclo para recorrer la secuencia
    for i in match:
        # si el valor de i es P1
        if i == "P1":
            # p1 aumenta en 1
            p1 += 1
            # si p1 es igual a 1
            if p1 == 1:
                # imprime el valor de p1 y el valor de p2
                print(f"{points[p1]} - {points[p2]}")
            # si p1 es igual a 2
            elif p1 == 2:
                # imprime el valor de p1 y el valor de p2
                print(f"{points[p1]} - {points[p2]}")
            # si p1 es igual a 3
            elif p1 == 3:
                # imprime el valor de p1 y el valor de p2
                print(f"{points[p1]} - {points[p2]}")
            # si p1 es igual a 4
            elif p1 == 4:
                # imprime el valor de p1 y el valor de p2
                print(f"{points[p1]} - {points[p2]}")
                # imprime Deuce
                print("Deuce")
            # si p1 es igual a 5
            elif p1 == 5:
                # imprime el valor de p1 y el valor de p2
                print(f"{points[p1]} - {points[p2]}")
                # imprime Ventaja P1
                print("Ventaja P1")
            # si p1 es igual a 6
            elif p1 == 6:
                # imprime el valor de p1 y el valor de p2
                print(f"{points[p1]} - {points[p2]}")
                # imprime Ha ganado el P1
                print("Ha ganado el P1")
                # rompe el ciclo
                break
        # si el valor de i es P2
        elif i == "P2":
            # p2 aumenta en 1
            p2 += 1
            # si p2 es igual a 1
            if p2 == 1:
                # imprime el valor de p1 y el valor de p2
                print(f"{points[p1]} - {points[p2]}")
    

def run():
    print("""Hola,
          
                soy un programa para calcular el resultado de un juego de tenis.
                Para esto debes seguir las siguientes indicaciones:
                
                1. Vamos a definir al jugador 1 y al jugador 2 como P1 y P2 respectivamente.
                2. Si un jugador gana un enfrentamiento debes colocarlo como un elemento de la secuencia.
                3. Colocar la secuencia separado por comas de la siguiente manera:
                    P1, P2, P1, P2, P1, P1 """)
    match = input_match()
    score(match)
  

if __name__ == '__main__':
    run()
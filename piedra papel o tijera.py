import random
import math


def jugar():

    jugador = input("Elige una de las siguientes opciones: 'P' para piedra, 'h' para Hoja y 't' para tijeras ")
    jugador = jugador.lower()
    lista = ["p", "h", "t"]
    ia = random.choice(lista)

    if jugador == ia:
        return(0, jugador, ia)

    if is_ganador(jugador, ia):
        return(1, jugador, ia)

    return (-1, jugador, ia)


def is_ganador(jugador, oponente):


    if (jugador == 'p' and oponente =='t') or (jugador =='h' and oponente=='p') and (jugador == 't' and oponente=='h'):
        return True
    return False


def el_mejor_jugador(n):


    jugador_ganador=0
    ia_ganador =0
    para_ganar = math.ceil(n/2)

    while jugador_ganador < para_ganar and ia_ganador < para_ganar:
        resultado, usuario, ia = jugar()
    
        if resultado == 0:
            print("Es un empate. Tu y la IA han elegido {}. \n".format(usuario))
        
    
        elif resultado == 1:
            jugador_ganador += 1
            print("Tu has elegido {} la IA {}. Ganastes \n".format(usuario, ia))

        else:
            ia_ganador += 1
            print("Tu has elegido {} y la IA {}. Perdistes \n".format(usuario, ia))


    if jugador_ganador > ia_ganador:
        print("Haz ganado lo mejor de {} juegos. endgame ".format(n))
    else:
        print('Desafortunadamente, la IA  ha hecho lo mejor de {} juegos. mejor suerte la proxima vex!:'.format(n))


if __name__ == "__main__":
    el_mejor_jugador(3)
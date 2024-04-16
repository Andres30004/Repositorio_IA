import time
import pyautogui
import random
import keyboard
# Espera unos segundos antes de comenzar para que tengas tiempo de abrir el emulador y el juego
time.sleep(5)
    



def activacion_aleatoria():
    opciones = [True, False]
    activar_funcion = random.choice(opciones)
    if activar_funcion:
        pyautogui.keyDown('d')

# Lista de funciones de movimiento
movimientos = [move_up, move_down, move_left, move_right]


# Bucle para ejecutar movimientos aleatorios hasta que se detenga manualmente
while True:
    time.sleep(5)
    movimiento_aleatorio = random.choice(movimientos)
    movimiento_aleatorio()



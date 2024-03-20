import time
import pyautogui
import random
# Espera unos segundos antes de comenzar para que tengas tiempo de abrir el emulador y el juego
time.sleep(5)

      
    
# Función para mover al personaje hacia arriba
def move_up():
    pyautogui.keyDown('w')
    time.sleep(0.5)  # Puedes ajustar este tiempo según sea necesario
    pyautogui.keyUp('w')

# Función para mover al personaje hacia abajo
def move_down():
    pyautogui.keyDown('s')
    time.sleep(0.5)
    pyautogui.keyUp('s')

# Función para mover al personaje hacia la izquierda
def move_left():
    pyautogui.keyDown('a')
    time.sleep(0.5)
    pyautogui.keyUp('a')

# Función para mover al personaje hacia la derecha
def move_right():
    pyautogui.keyDown('d')
    time.sleep(0.5)
    pyautogui.keyUp('d')


def pynput():
    while True:       
            # Lista de letras disponibles
            letras = ['w','s','a','d']
            # Seleccionar una letra aleatoria de la lista
            letra_aleatoria = random.choice(letras)
        # Hacer algo en cada iteración del bucle
            repeticiones = random.randint(5, 10)
            for _ in range(repeticiones):
                pyautogui.press(letra_aleatoria)  

# Ejemplo de cómo usar las funciones para mover al personaje
time.sleep(5)    
move_up()
move_right()
move_down()
move_left()

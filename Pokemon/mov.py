import time
import pyautogui
import random
import keyboard
from pynput import mouse
import threading

# Espera unos segundos antes de comenzar para que tengas tiempo de abrir el emulador y el juego
time.sleep(5)
# Bandera para indicar si ha ocurrido algún movimiento
movimiento_detectado = False
    
opciones = [True, False]
activar_funcion = random.choice(opciones)


# Función para mover al personaje hacia arriba
def move_up():

    pyautogui.keyDown('w')
    time.sleep(random.randint(0, 3))  # Puedes ajustar este tiempo según sea necesario
    pyautogui.keyUp('w')
    pyautogui.keyDown('w')
    time.sleep(random.randint(0, 1))  # Puedes ajustar este tiempo según sea necesario
    pyautogui.keyUp('w')
    activar_funcion = random.choice(opciones)
    if activar_funcion:
        pyautogui.keyDown('l')
        time.sleep(random.randint(0,1))
    pyautogui.keyUp('l')

# Función para mover al personaje hacia abajo
def move_down():
    pyautogui.keyDown('s')
    time.sleep(random.randint(0, 3))
    pyautogui.keyUp('s')
    pyautogui.keyDown('s')
    time.sleep(random.randint(0, 1))
    pyautogui.keyUp('s')
    activar_funcion = random.choice(opciones)
    if activar_funcion: 
        pyautogui.keyDown('l')
        time.sleep(random.randint(0,1))
    pyautogui.keyUp('l')

# Función para mover al personaje hacia la izquierda
def move_left():
    pyautogui.keyDown('a')
    time.sleep(random.randint(0, 3))
    pyautogui.keyUp('a')
    pyautogui.keyDown('a')
    time.sleep(random.randint(0, 1))
    pyautogui.keyUp('a')
    activar_funcion = random.choice(opciones)
    if activar_funcion:
        pyautogui.keyDown('l')
        time.sleep(random.randint(0,1))
    pyautogui.keyUp('l')

# Función para mover al personaje hacia la derechaalwla
def move_right():
    pyautogui.keyDown('d')
    time.sleep(random.randint(0, 3))
    pyautogui.keyUp('d')
    pyautogui.keyDown('d')
    time.sleep(random.randint(0, 1))
    pyautogui.keyUp('d')
    activar_funcion = random.choice(opciones)
    if activar_funcion:
        pyautogui.keyDown('l')
        time.sleep(random.randint(0,1))
    pyautogui.keyUp('l')


# Lista de funciones de movimiento
movimientos = [move_up, move_down, move_left, move_right]

# Función que se ejecuta cuando hay movimiento del mouse
def on_move(x, y):
    global movimiento_detectado
    movimiento_detectado = True
    print(f'Movimiento del mouse detectado en {x}, {y}')

# Función para verificar la inactividad del mouse
def verificar_inactividad(tiempo_limite):
    global movimiento_detectado
    if not movimiento_detectado:
        print("No se ha detectado movimiento del mouse.")
        time.sleep(5)
        while True:
            movimiento_aleatorio = random.choice(movimientos)
            movimiento_aleatorio()
            movimiento_detectado = False
    threading.Timer(tiempo_limite, verificar_inactividad, [tiempo_limite]).start()

# Crear un listener para el movimiento del mouseDDWWWWAAAASSSSSSDDWWAADDAADDDDWWLAASSAADDDDSSSSSSAASSW
with mouse.Listener(on_move=on_move) as listener:
    time.sleep(5)
    verificar_inactividad(15)  # Establecer el tiempo límite de inactividad en segundos
    listener.join()


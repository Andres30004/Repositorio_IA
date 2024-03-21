import time
import pyautogui
import random
import keyboard
# Espera unos segundos antes de comenzar para que tengas tiempo de abrir el emulador y el juego


# Función para mover al personaje hacia arriba
def move_up():
    pyautogui.keyDown('w')
    time.sleep(random.randint(0, 3))  # Puedes ajustar este tiempo según sea necesario
    pyautogui.keyUp('w')
    pyautogui.keyDown('w')
    time.sleep(random.randint(0, 1))  # Puedes ajustar este tiempo según sea necesario
    pyautogui.keyUp('w')
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
    pyautogui.keyDown('l')
    time.sleep(random.randint(0,1))
    pyautogui.keyUp('l')



# Lista de funciones de movimiento
movimientos = [move_up, move_down, move_left, move_right]

# Función para verificar si se ha presionado alguna tecla durante un intervalo de tiempo
def check_key_pressed(interval):
    start_time = time.time()
    while time.time() - start_time < interval:
        if keyboard.is_pressed('w') or keyboard.is_pressed('a') or keyboard.is_pressed('s') or keyboard.is_pressed('d'):
            return True
        time.sleep(0.1)  # Pequeño tiempo de espera para no sobrecargar el CPU
    return False

# Bucle para ejecutar movimientos aleatorios después de detectar inactividad en el teclado
while True:
    if not check_key_pressed(60*5):  # Espera 5 minutos de inactividad en el teclado
        movimiento_aleatorio = random.choice(movimientos)
        movimiento_aleatorio()
# Bucle para ejecutar movimientos aleatorios hasta que se detenga manualmente
while True:
    time.sleep(5)
    movimiento_aleatorio = random.choice(movimientos)
    movimiento_aleatorio()



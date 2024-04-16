from pynput import mouse
import threading
import time

# Bandera para indicar si ha ocurrido algún movimiento
movimiento_detectado = False

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
        movimiento_aleatorio = random.choice(movimientos)
        movimiento_aleatorio()
        movimiento_detectado = False
    threading.Timer(tiempo_limite, verificar_inactividad, [tiempo_limite]).start()

# Crear un listener para el movimiento del mouse
with mouse.Listener(on_move=on_move) as listener:
    verificar_inactividad(15)  # Establecer el tiempo límite de inactividad en segundos
    listener.join()


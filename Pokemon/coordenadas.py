import pyautogui

try:
    # Bucle infinito para obtener continuamente las coordenadas
    while True:
        # Obtener las coordenadas actuales del cursor
        x, y = pyautogui.position()
        
        # Imprimir las coordenadas
        print(f"Las coordenadas del cursor son: x={x}, y={y}")

        # Esperar un corto período de tiempo antes de obtener las coordenadas nuevamente
        pyautogui.sleep(0)  # Esperar 1 segundo
except KeyboardInterrupt:
    print("\nPrograma terminado por el usuario.")
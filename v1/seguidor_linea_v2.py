from motores import carro
from sensores import Qti
from time import sleep
from llist import LinkedList
from machine import Pin

# --- Inicialización de componentes ---
autito = carro(13, 14)

# Sensores QTI y LEDs de estado
qtis = [Qti(6), Qti(8), Qti(10), Qti(12)]
leds = [Pin(i+2, Pin.OUT) for i in range(4)]

# Umbrales de detección (ajustar según calibración)
umbrales = [2000, 2000, 2000, 2000]

# --- Diccionarios de acciones por estrategia ---

acciones_seguidor = {
    # Derecha
    (0, 0, 1, 0): autito.girar_derecha,
    (0, 0, 1, 1): autito.girar_derecha,
    (0, 1, 1, 1): autito.girar_derecha,
    (0, 0, 0, 1): autito.girar_derecha,
    # Izquierda
    (1, 0, 0, 0): autito.girar_izquierda,
    (1, 1, 0, 0): autito.girar_izquierda,
    (1, 1, 1, 0): autito.girar_izquierda,
    (0, 1, 0, 0): autito.girar_izquierda,
    # Nodo especial
    (1, 1, 1, 1): contar_hitos,
}

acciones_informacion = {
    # Derecha
    (0, 0, 1, 0): autito.girar_derecha,
    # Izquierda
    (0, 1, 0, 0): autito.girar_izquierda,
    # Información
    (0, 0, 1, 1): info_derecha,
    (0, 1, 1, 1): info_derecha,
    (0, 0, 0, 1): info_derecha,
    (1, 0, 0, 0): info_izquierda,
    (1, 1, 0, 0): info_izquierda,
    (1, 1, 1, 0): info_izquierda,
    # Nodo especial
    (1, 1, 1, 1): contar_hitos,
}
#### FALTA DEFINIR acciones_entrar_cuadrado y acciones_salir_cuadrado #####

# --- Pista con secuencia de estrategias ---
pista = LinkedList()
pista.append(acciones_seguidor)
pista.append(acciones_seguidor)
pista.append(acciones_seguidor)
pista.append(acciones_informacion)
pista.append(acciones_entrar_cuadrado)
pista.append(acciones_salir_cuadrado)
pista.append(acciones_seguidor)

# --- Loop principal ---
acciones = pista.pop()

while True:
    # Lectura de sensores
    qtis_valores = [qti.medir() for qti in qtis]
    detecciones = tuple(int(valor > umbral) for valor, umbral in zip(qtis_valores, umbrales))
    print(detecciones)

    # Actualización de LEDs
    for led, estado in zip(leds, detecciones):
        led.value(estado)

    # Selección y ejecución de acción
    accion = acciones.get(detecciones, autito.avanzar)
    accion()

    sleep(0.1)

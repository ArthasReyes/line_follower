from machine import Pin, ADC
from movil import Movil
from ads1115 import ADS1115
from time import sleep, sleep_ms
from llist import LinkedList
from pistas import *


#Componentes
motor1 = motorDC_A(1,2)
motor2 = motorDC_B(3,4)

autito = Movil(motor1,motor2)
ads = ADS1115(sda_pin=14, scl_pin=15)

#setup
qti_pines = [0, 1, 2, 3]  # Pines de los sensores QTI en el I2C
umbrales = [2000, 2000, 2000, 2000] #calibrar


acciones_seguidor= {
    #derecha
    (0, 0, 1, 0): autito.girar_derecha,
    (0, 0, 1, 1): autito.girar_derecha,
    (0, 1, 1, 1): autito.girar_derecha,
    (0, 0, 0, 1): autito.girar_derecha,
    #izquierda
    (1, 0, 0, 0): autito.girar_izquierda,
    (1, 1, 0, 0): autito.girar_izquierda,
    (1, 1, 1, 0): autito.girar_izquierda,
    (0, 1, 0, 0): autito.girar_izquierda,
    #salto
    (1, 1, 1, 1): autito.salto,
}

acciones_informacion= {
    #derecha
    (0, 0, 1, 0): autito.girar_derecha,
    #izquierda
    (0, 1, 0, 0): autito.girar_izquierda,
    #info
    (0, 0, 1, 1): info_derecha,
    (0, 1, 1, 1): info_derecha,
    (0, 0, 0, 1): info_derecha,
    (1, 0, 0, 0): info_izquierda,
    (1, 1, 0, 0): info_izquierda,
    (1, 1, 1, 0): info_izquierda,
    #salto
    (1, 1, 1, 1): autito.salto,
}

acciones_entrar_cuadrado= {
    
}

pista = Linked_list()
pista.append(acciones_seguidor)
pista.append(acciones_informacion)
pista.append(acciones_entrar_cuadrado)
pista.append(acciones_salir_cuadrado)
pista.append(acciones_seguidor)


acciones = pista.pop()
while True:
    #sensores
    sensores_valores = [ads.leer(0,pin) for pin in qti_pines]
    detecciones = tuple(int(valor > umbral) for valor, umbral in zip(sensores_valores, umbrales))
    print(detecciones)
    
    #logica
    accion = acciones.get(detecciones, autito.avanzar)

    #loop
    accion()
    sleep_ms(100)

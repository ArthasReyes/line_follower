import math
from sensores import Qti
from machine import Pin
from time import sleep

qtis = [Qti(pin) for pin in [2,3,4,5]]
boton = Pin(0, Pin.IN)

def calcular_umbral(blancos, negros):
    cb = sum(blancos)/len(blancos)
    cn = sum(negros)/len(negros)

    rb = int(math.sqrt(sum(abs(x - cb) for x in blancos) / len(blancos)))
    rn = int(math.sqrt(sum(abs(x - cn) for x in negros) / len(negros)))
    
    cb = int(cb)
    cn = int(cn)

    umbral = int(cb + (cn-cb)/(rn+rb)*rb)
    return umbral

def leer_sensores():
    while True:
        print("leyendo")
        if(boton.value == 0):
            mediciones = [qti.medir() for qti in qtis]
            print("lectura: ": mediciones)
            return mediciones
        sleep(1)

def main():
    blancos = []
    for i in range(5):
        blancos.append(leer_sensores())
    
    negros = []
    for i in range(5):
        negros.append(leer_sensores())
    
    blancos = [list(row) for row in zip(*blancos)]
    negros = [list(row) for row in zip(*negros)]

    umbrales = [calcular_umbral(blanco, negro) for blanco, negro in zip(blancos, negros)]
    print(umbrales)

main()

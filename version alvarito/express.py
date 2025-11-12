from sensores import Qti, Ultrasonico
from machine import Pin
from time import sleep
from auto import Auto, AutoDummy
sleep(5)

#########################
##### CONEXIONES ########
#########################

auto = Auto(9,7,11,1)
#auto = AutoDummy()

qti0=Qti(8)
qti1=Qti(6)
qti2=Qti(10)
qti3=Qti(12)
us = Ultrasonico(18, 19)
led0 = Pin(2, Pin.OUT)
led1 = Pin(3, Pin.OUT)
led2 = Pin(4, Pin.OUT)
led3 = Pin(5, Pin.OUT)

#########################
#### CONFIGURACIONES ####
#########################

umbral0 = 1391
umbral1 = 1958
umbral2 = 2006 
umbral3 = 2273
d = 0
contador = 0
vel_lenta = 10
vel_normal = 20
vel_rapida = 40
vel_derecha = 60
vel_izquierda = 60

while True:
    #########################
    ##### LEER SENSORES #####
    #########################

    vqti0 = qti0.medir()
    vqti1 = qti1.medir()
    vqti2 = qti2.medir()
    vqti3 = qti3.medir()
    if contador == 0:
        d = us.medir()
    elif contador == 1:
        d = us.medir()
    elif contador == 2:
        d = us.medir()
        
    caso = [vqti0 > umbral0, vqti1 > umbral1, vqti2 > umbral2, vqti3 > umbral3]
    #print("------ \n", vqti0, vqti1, vqti2, vqti3, d, contador, "\n", caso)
    
    led0.on() if caso[0] else led0.off()
    led1.on() if caso[1] else led1.off()
    led2.on() if caso[2] else led2.off()
    led3.on() if caso[3] else led3.off()

    #########################
    ###### DECISIONES #######
    #########################
    
    if contador == 0 and 0 < d < 5:
        auto.esquivar_izquierda()
        contador = contador + 1
        auto.salto()
    elif contador == 1 and 0 < d < 5:
        auto.derecha(600) #180 grados
        contador = contador + 1
        auto.salto()
    elif contador == 2 and 0 < d < 5:
        auto.esquivar_derecha()
        contador = contador + 1
        auto.salto()
    
    
    #casos bases
    if   caso == [0,0,0,0]: auto.avanzar(vel_normal)
    elif caso == [0,1,0,0]: auto.izquierda(vel_izquierda)
    elif caso == [0,0,1,0]: auto.derecha(vel_derecha)
    #casos interesantes
    elif caso == [1,1,0,0] or caso == [1,0,0,0] or caso == [1,1,1,0]: auto.izquierda(vel_izquierda)
    elif caso == [0,0,1,1] or caso == [0,0,0,1] or caso == [0,1,1,1]: auto.derecha(vel_derecha)
    elif caso == [0,1,1,0]: auto.avanzar(vel_normal)
    elif caso == [1,1,1,1]:
        if contador == 3:
            auto.parar()
            break
            
        else:
            auto.salto()
            contador = contador +1
    #casos imposibles
    elif caso == [1,0,1,0]: auto.avanzar(vel_lenta)
    elif caso == [0,1,0,1]: auto.avanzar(vel_lenta)
    elif caso == [1,1,0,1]: auto.avanzar(vel_lenta)
    elif caso == [1,0,1,1]: auto.avanzar(vel_lenta)
    elif caso == [1,0,0,1]: auto.avanzar(vel_lenta)
    
    #########################
    ##### FIN DE CICLO ######
    #########################    
    auto.parar()
    sleep (0.1)
    


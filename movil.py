from machine import Pin, PWM, I2C
from time import sleep

class motorDC:
    def __init__(self, pin1:int, pin2:int):
        self.pin1 = Pin(pin1, Pin.OUT)
        self.pin2 = Pin(pin2, Pin.OUT)
        
    def girar_cw(self):
        pass
    
    def girar_ccw(self):
        pass
    
    def detener(self):
        self.pin1.off()
        self.pin2.off()

class motorDC_A(motorDC):
    def girar_cw(self):
        self.pin1.on()
        self.pin2.off()
    
    def girar_ccw(self):
        self.pin1.off()
        self.pin2.on()

class motorDC_B(motorDC):
    def girar_cw(self):
        self.pin1.off()
        self.pin2.on()
    
    def girar_ccw(self):
        self.pin1.on()
        self.pin2.off()

class Movil:
    def __init__(self, motor1: motorDC, motor2: motorDC):
        self.motor1 = motor1
        self.motor2 = motor2
        
    def avanzar(self):
        self.motor1.girar_cw()
        self.motor2.girar_ccw()
        
    def detener(self):
        self.motor1.detener()
        self.motor2.detener()
        
    def girar_derecha(self):
        self.motor1.girar_cw()
        self.motor2.girar_cw()
        
    def girar_izquierda(self):
        self.motor1.girar_ccw()
        self.motor2.girar_ccw()
    
    def retroceder(self):
        self.motor1.girar_ccw()
        self.motor2.girar_cw()
    
    def saltar(self):
        self.avanzar()
        sleep(0.4)
        self.detener()
    
    def girar_90izq(self):
        pass
    
    def girar_90der(self):
        pass
    
    def esquivar(self):
        pass

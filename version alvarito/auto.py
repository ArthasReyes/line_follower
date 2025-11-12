from machine import Pin
from time import sleep_ms
class AutoDummy:
    def __init__(self, MP1I, MP2I, MP3D, MP4D): pass
    def avanzar(self, tiempo=0.005): print("avanzar")
    def derecha(self, tiempo=0.005):print("derecha")
    def izquierda(self, tiempo=0.005): print("izquierda")
    def parar(self): print("parar")
    def salto(self):print("salto")
    def cderecha(self):print("cderecha")
    def cizquierda(self): print("cizquierda")
    def esquivar(self): print("esquivar")

    
class Auto:
    def __init__(self, MP1I, MP2I, MP3D, MP4D):
        #conexiones y configuraciones
        self.MP1I = Pin ( MP1I, Pin.OUT)                                    # pines a lo mejro del motor cambian alvaro del futuro
        self.MP2I = Pin ( MP2I, Pin.OUT)
                             
        self.MP3D = Pin ( MP3D, Pin.OUT)
        self.MP4D = Pin ( MP4D, Pin.OUT)


    #los cosos de avanzar y todo eso
    def avanzar(self, tiempo=50):              
        self.MP1I.on()
        self.MP2I.off()
        
        self.MP3D.on()
        self.MP4D.off()
        
        sleep_ms(tiempo)

    def derecha(self, tiempo=150):
        self.MP1I.on() 
        self.MP2I.off()
        
        self.MP3D.off()
        self.MP4D.on()
        
        sleep_ms(tiempo)

    def izquierda(self, tiempo=150):
        self.MP1I.off()
        self.MP2I.on()
        
        self.MP3D.on()
        self.MP4D.off()
        sleep_ms(tiempo)

        
    def parar(self):
        self.MP1I.off()
        self.MP2I.off()
        
        self.MP3D.off()
        self.MP4D.off()
        
        
    def salto(self):
        self.avanzar(300)
        
    def cderecha(self):
        self.avanzar(0.1)
        self.derecha(650)
        
    def cizquierda(self):      
        self.izquierda(600)
        
    def esquivar(self):
        self.derecha(650)
        self.parar()
        self.avanzar(800)
        self.parar()
        self.izquierda(600)
        self.parar()
        self.avanzar(500)
        self.parar()
        self.izquierda(600)
        self.parar()
        self.avanzar(500)
        self.parar()
        self.derecha(650)
        self.parar()
        self.avanzar(500)
        self.parar()
        sleep_ms(1000)

    def esquivar_derecha(self):
        self.derecha(650)
        self.parar()
        self.avanzar(800)
        self.parar()
        self.izquierda(600)
        self.parar()
        self.avanzar(500)
        self.parar()
        self.izquierda(600)
        self.parar()
        self.avanzar(500)
        self.parar()
        self.derecha(650)
        self.parar()
        self.avanzar(500)
        self.parar()
        sleep_ms(1000)

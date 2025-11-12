# Casos posibles: 0 blanco, 1 negro

acciones_base= {
    #adelante
    (0, 0, 0, 0): autito.avanzar,
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
    
    #casos raros
    (1, 0, 1, 1): autito.avanzar,
    (1, 0, 1, 0): autito.avanzar,
    (0, 1, 1, 0): autito.avanzar,
    (1, 0, 0, 1): autito.avanzar,
    (0, 1, 0, 1): autito.avanzar,
    (1, 1, 0, 1): autito.avanzar,
    #salto
    (1, 1, 1, 1): autito.salto,
}

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


# Casos posibles: 0 blanco, 1 negro
acciones_informacion= {
    #derecha
    (0, 0, 1, 0): autito.girar_derecha,
    (0, 0, 1, 1): info_derecha,
    (0, 1, 1, 1): info_derecha,
    (0, 0, 0, 1): info_derecha,
    #izquierda
    (1, 0, 0, 0): info_izquierda,
    (1, 1, 0, 0): info_izquierda,
    (1, 1, 1, 0): info_izquierda,
    (0, 1, 0, 0): autito.girar_izquierda,
    #salto
    (1, 1, 1, 1): autito.salto,
}

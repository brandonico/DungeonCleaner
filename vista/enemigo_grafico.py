import pygame
from vista.personaje_grafico import PersonajeGrafico
from vista.animacion import AnimacionEnemiga

ANCHO_FRAME, ALTO_FRAME = 191, 191

class EnemigoGrafico(PersonajeGrafico):
    """
    Representa un enemigo gráfico en pantalla, heredando de PersonajeGrafico.
    """
    def __init__(self, x, y, color, modelo):
        super().__init__(x, y, color, modelo)
        self.rect = pygame.Rect(x - 10, y, 50, 50)
        self.animacion = AnimacionEnemiga(ANCHO_FRAME, ALTO_FRAME)
        self.direccion_animacion = "izquierda"  # Dirección por defecto


        
    def mover(self, direccion, cantidad):
        """
        Mueve el personaje en una dirección dada.

        direccion: 'arriba', 'abajo', 'izquierda' o 'derecha'.
        cantidad: desplazamiento en píxeles.
        ANCHO, ALTO: límites de la pantalla para evitar salir.
        """
        
        if direccion == "izquierda" or direccion == "derecha":
            self.direccion_animacion = direccion  # Guarda la dirección actual
        self.direccion_de_ataque = direccion 

        if direccion == "arriba":   #movimiento para arriba
            self.rect.y -= cantidad     #movimineto del personaje
            
        elif direccion == "abajo":
            self.rect.y += cantidad
            
        elif direccion == "izquierda":
            self.rect.x -= cantidad
           
        elif direccion == "derecha":
            self.rect.x += cantidad
            
        if not self.en_ataque:
            self.animacion.actualizar(f"{self.direccion_animacion}", "caminando")  #actualiza la animacion del personaje

    def dibujar(self, pantalla):
        """
        Dibuja el personaje sobre la superficie dada.

        pantalla: superficie donde se dibuja.
        """
        # Dibuja el personaje
        #pygame.draw.rect(pantalla, self.color, self.rect)

        #dibuja el sprite sobre el rectángulo del personaje
        x = self.rect.x + 5 + (self.rect.width - self.animacion.imagen_actual.get_width()) // 2
        y = self.rect.y + (self.rect.height - self.animacion.imagen_actual.get_height()) // 2
        pantalla.blit(self.animacion.imagen_actual, (x, y))

    
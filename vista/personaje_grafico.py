import pygame
### 🧩 Clase base:
class PersonajeGrafico:
    """
    Representa un personaje gráfico en pantalla.

    Atributos:
    rect: Rectángulo que define su posición y tamaño.
    color: Color con el que se dibuja.
    """
    def __init__(self, x, y, color, modelo):
    def __init__(self, x, y, color, modelo):
        """
        Inicializa la posición y color del personaje.

        x, y: coordenadas iniciales.
        color: tupla RGB.
        """
        self.rect = pygame.Rect(x, y, 60, 60)
        self.color = color
        self.modelo = modelo
        self.modelo = modelo

    def mover(self, direccion, cantidad, ANCHO, ALTO):
        """
        Mueve el personaje en una dirección dada.

        direccion: 'arriba', 'abajo', 'izquierda' o 'derecha'.
        cantidad: desplazamiento en píxeles.
        ANCHO, ALTO: límites de la pantalla para evitar salir.
        """
        if direccion == "arriba":
            self.rect.y -= cantidad
        elif direccion == "abajo":
            self.rect.y += cantidad
        elif direccion == "izquierda":
            self.rect.x -= cantidad
        elif direccion == "derecha":
            self.rect.x += cantidad

        if self.rect.left < 0:
            self.rect.left = 0
        if self.rect.right > ANCHO:
            self.rect.right = ANCHO
        if self.rect.top < 0:
            self.rect.top = 0
        if self.rect.bottom > ALTO:
            self.rect.bottom = ALTO

    def dibujar(self, pantalla):
        """
        Dibuja el personaje sobre la superficie dada.

        pantalla: superficie donde se dibuja.
        """
        pygame.draw.rect(pantalla, self.color, self.rect)

    def colisiona_con(self, otro):  
        """
        Detecta si colisiona con otro personaje.

        otro: otro PersonajeGrafico.
        Devuelve: True si colisionan.
        """
        return self.rect.colliderect(otro.rect)
    
    def atacar_a(self, otro):
        """
        Ataca a otro personaje.

        otro: otro PersonajeGrafico.
        """
        self.modelo.atacar(otro.modelo)
    
    def atacar_a(self, otro):
        """
        Ataca a otro personaje.

        otro: otro PersonajeGrafico.
        """
        self.modelo.atacar(otro.modelo)
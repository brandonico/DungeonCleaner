import pygame
from vista.animacion import Animacion


AMARILLO = (200, 200, 0)    #constante para el color del hitbox del arma
ANCHO_FRAME, ALTO_FRAME = 191, 191

### 🧩 Clase base:
class PersonajeGrafico(pygame.sprite.Sprite):  # <-- Cambia aquí
    """
    Representa un personaje gráfico en pantalla.

    Atributos:
    rect: Rectángulo que define su posición y tamaño.
    color: Color con el que se dibuja.
    """
    def __init__(self, x, y, color, modelo):
        super().__init__()  # <-- Llama al constructor de Sprite
        """
        Inicializa la posición y color del personaje.

        x, y: coordenadas iniciales.
        color: tupla RGB.
        modelo: instancia del modelo lógico asociado al personaje.
        """
        self.x = x
        self.y = y
        self.rect = pygame.Rect(x, y, 30, 45)
        self.color = color
        self.modelo = modelo    #modelo es una instancia de Personaje o Jugador
        

        self.animacion = Animacion(ANCHO_FRAME, ALTO_FRAME)
        self.direccion_animacion = "derecha"  # Dirección por defecto
        self.direccion_de_ataque = "derecha"  # Dirección de ataque por defecto
        self.en_ataque = False

        self.arma = pygame.Rect(x + 30, y, 65, 45)   #posicion a la derecha

    def mover(self, direccion, cantidad, ANCHO, ALTO, en_ataque=False):
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
            self.arma = pygame.Rect(self.rect.x - 50, self.rect.y - 45, 135, 50)
            
        elif direccion == "abajo":
            self.rect.y += cantidad
            self.arma = pygame.Rect(self.rect.x - 20, self.rect.y + 45, 110, 60)
            
        elif direccion == "izquierda":
            self.rect.x -= cantidad
            self.arma = pygame.Rect(self.rect.x - 65, self.rect.y, 65, 45)
           
        elif direccion == "derecha":
            self.rect.x += cantidad
            self.arma = pygame.Rect(self.rect.x + 30, self.rect.y, 65, 45)

        if not self.en_ataque:
            self.animacion.actualizar(f"{self.direccion_animacion}", "caminando")  #actualiza la animacion del personaje

        # Limitar el movimiento dentro de los límites de la pantalla
        if self.rect.left < 0:
            self.rect.left = 0
        if self.rect.right > ANCHO:
            self.rect.right = ANCHO
        if self.rect.top < 0:
            self.rect.top = 0
        if self.rect.bottom > ALTO:
            self.rect.bottom = ALTO

    def quieto(self):
        """
        Mantiene al personaje en su posición actual sin moverse.
        Actualiza la animación a "quieto".
        """
        self.animacion.actualizar(self.direccion_animacion, "quieto")

    def dibujar(self, pantalla):
        """
        Dibuja el personaje sobre la superficie dada.

        pantalla: superficie donde se dibuja.
        """
        # Dibuja el personaje
        #pygame.draw.rect(pantalla, self.color, self.rect)
        #pygame.draw.rect(pantalla, AMARILLO, self.arma)

        #dibuja el sprite sobre el rectángulo del personaje
        x = self.rect.x + (self.rect.width - self.animacion.imagen_actual.get_width()) // 2
        y = self.rect.y + (self.rect.height - self.animacion.imagen_actual.get_height()) // 2
        pantalla.blit(self.animacion.imagen_actual, (x, y))

    def colisiona_con(self, otro):  
        """
        Detecta si colisiona con otro personaje.

        otro: otro PersonajeGrafico.
        Devuelve: True si colisionan.
        """
        return self.rect.colliderect(otro.rect)
    
    def ataque(self, atacando=False):
        """
        Realiza un ataque, actualizando la animación a "ataque".
        """
        self.en_ataque = atacando
        if atacando:
            self.animacion.actualizar(self.direccion_de_ataque, "ataque")
    
    def atacar_a(self, otro):
        """
        Ataca a otro personaje.

        otro: otro PersonajeGrafico.
        """
        self.modelo.atacar(otro.modelo)
    
    def muere(self):
        if self.modelo.salud <= 0:
            self.animacion.muerte(False)
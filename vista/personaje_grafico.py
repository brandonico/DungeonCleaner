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
        """
        Inicializa la posición y color del personaje.

        x, y: coordenadas iniciales.
        color: tupla RGB.
        modelo: instancia del modelo lógico asociado al personaje.
        """
        self.rect = pygame.Rect(x, y, 60, 60)
        self.color = color
        self.modelo = modelo    #modelo es una instancia de Personaje o Jugador

        # Crear una superficie para el arma
        self.arma_surface = None
        self.arma_angle = 0  # Ángulo inicial del arma
        self.arma_pos = (self.rect.x + 20, self.rect.y + 20)  # Posición inicial del arma
        self.arma_rect = None  # Inicializar arma_rect como None

        if hasattr(self.modelo, 'arma') and self.modelo.arma:
            # Cambiar el tamaño del arma para que sea más larga
            self.arma_surface = pygame.Surface((80, 10), pygame.SRCALPHA)  # Ancho: 80, Alto: 10
            self.arma_surface.fill((200, 200, 0))  # Color amarillo para el arma
            self.arma_rect = pygame.Rect(self.arma_pos[0], self.arma_pos[1], 80, 10)  # Rectángulo del arma

    def mover(self, direccion, cantidad, ANCHO, ALTO):
        """
        Mueve el personaje en una dirección dada.

        direccion: 'arriba', 'abajo', 'izquierda' o 'derecha'.
        cantidad: desplazamiento en píxeles.
        ANCHO, ALTO: límites de la pantalla para evitar salir.
        """
        if direccion == "arriba":
            self.rect.y -= cantidad
            if self.arma_surface:
                self.arma_angle = 0  # Apunta hacia arriba
                self.arma_pos = (self.rect.x + 25, self.rect.y - 20)  # Centrar horizontalmente
                self.arma_surface = pygame.Surface((10, 80), pygame.SRCALPHA)  # Alto: 80, Ancho: 10
                self.arma_surface.fill((200, 200, 0))  # Color amarillo
                self.arma_rect = pygame.Rect(self.arma_pos[0], self.arma_pos[1], 10, 80)
        elif direccion == "abajo":
            self.rect.y += cantidad
            if self.arma_surface:
                self.arma_angle = 180  # Apunta hacia abajo
                self.arma_pos = (self.rect.x + 25, self.rect.y + self.rect.height)
                self.arma_surface = pygame.Surface((10, 80), pygame.SRCALPHA)  # Alto: 80, Ancho: 10
                self.arma_surface.fill((200, 200, 0))  # Color amarillo
                self.arma_rect = pygame.Rect(self.arma_pos[0], self.arma_pos[1], 10, 80)
        elif direccion == "izquierda":
            self.rect.x -= cantidad
            if self.arma_surface:
                self.arma_angle = 0  # Apunta hacia la izquierda (horizontal, sin rotación)
                self.arma_pos = (self.rect.x - 80, self.rect.y + 25)  # Centrar verticalmente
                self.arma_surface = pygame.Surface((80, 10), pygame.SRCALPHA)  # Ancho: 80, Alto: 10
                self.arma_surface.fill((200, 200, 0))  # Color amarillo
                self.arma_rect = pygame.Rect(self.arma_pos[0], self.arma_pos[1], 80, 10)
        elif direccion == "derecha":
            self.rect.x += cantidad
            if self.arma_surface:
                self.arma_angle = 0  # Apunta hacia la derecha (horizontal, sin rotación)
                self.arma_pos = (self.rect.x + self.rect.width, self.rect.y + 25)
                self.arma_surface = pygame.Surface((80, 10), pygame.SRCALPHA)  # Ancho: 80, Alto: 10
                self.arma_surface.fill((200, 200, 0))  # Color amarillo
                self.arma_rect = pygame.Rect(self.arma_pos[0], self.arma_pos[1], 80, 10)

        # Limitar el movimiento dentro de los límites de la pantalla
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
        # Dibuja el personaje
        pygame.draw.rect(pantalla, self.color, self.rect)

        # Dibuja el arma con rotación
        if self.arma_surface:
            arma_rotada = pygame.transform.rotate(self.arma_surface, self.arma_angle)
            arma_rect = arma_rotada.get_rect(center=(self.arma_pos[0] + 20, self.arma_pos[1] + 5))
            pantalla.blit(arma_rotada, arma_rect.topleft)

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
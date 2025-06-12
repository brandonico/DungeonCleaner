import pygame
import sys

class Controlador:
    def __init__(self, jugador1, jugador2, ancho, alto):
        self.jugador1 = jugador1
        self.jugador2 = jugador2
        self.ancho = ancho
        self.alto = alto
        self.tiempo_ultimo_danio = 0
        self.intervalo_danio = 2000  # milisegundos

    def manejar_eventos(self):
        teclas = pygame.key.get_pressed() 
        #guardamos posiciones actuales
        #crear una copia independiente de rect_azul, un nuevo rectángulo con las mismas coordenadas y tamaño, pero que podemos modificar sin afectar aún al original.
    
        # Movimiento del rectángulo rojo con W, A, S, D
        if teclas[pygame.K_w]:
            self.jugador1.mover("arriba", self.jugador1.modelo.velocidad_movimiento, self.ancho, self.alto)
        if teclas[pygame.K_s]:
            self.jugador1.mover("abajo", self.jugador1.modelo.velocidad_movimiento, self.ancho, self.alto)
        if teclas[pygame.K_a]:
            self.jugador1.mover("izquierda", self.jugador1.modelo.velocidad_movimiento, self.ancho, self.alto)
        if teclas[pygame.K_d]:
            self.jugador1.mover("derecha", self.jugador1.modelo.velocidad_movimiento, self.ancho, self.alto)

        # Movimiento automático del jugador2 persiguiendo a jugador1
        dx = self.jugador1.rect.x - self.jugador2.rect.x
        dy = self.jugador1.rect.y - self.jugador2.rect.y

        if abs(dx) > abs(dy):
            if dx > 0:
                self.jugador2.mover("derecha", self.jugador2.modelo.velocidad_movimiento, self.ancho, self.alto)
            elif dx < 0:
                self.jugador2.mover("izquierda", self.jugador2.modelo.velocidad_movimiento, self.ancho, self.alto)
        else:
            if dy > 0:
                self.jugador2.mover("abajo", self.jugador2.modelo.velocidad_movimiento, self.ancho, self.alto)
            elif dy < 0:
                self.jugador2.mover("arriba", self.jugador2.modelo.velocidad_movimiento, self.ancho, self.alto)

    def verificar_colision_y_danio(self, tiempo_actual):
        if self.jugador1.colisiona_con(self.jugador2):
            if tiempo_actual - self.tiempo_ultimo_danio > self.intervalo_danio:
                self.jugador1.modelo.recibir_danio(self.jugador2.modelo.ataque)
                self.tiempo_ultimo_danio = tiempo_actual
            if self.jugador1.modelo.salud <= 0:
                pygame.quit()
                sys.exit()

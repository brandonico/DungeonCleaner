import pygame
import sys

class Controlador:
    """Sen encarga del movimiento de los personajes dentro del juego
    y la administracion de las colisiones entre ellos."""
    def __init__(self, jugador1, jugador2, ancho, alto):
        self.jugador1 = jugador1
        self.jugador2 = jugador2
        self.ancho = ancho
        self.alto = alto
        self.tiempo_ultimo_danio = 0
        self.intervalo_danio = 2000  # milisegundos

    def manejar_eventos(self):
        """esta clase sirve para manejar los controles del jugador
        y el movimiento del oponente"""
        teclas = pygame.key.get_pressed() 

        # Movimiento del rectángulo rojo con W, A, S, D
        if teclas[pygame.K_w]:
            self.jugador1.mover("arriba", self.jugador1.modelo.velocidad_movimiento, self.ancho, self.alto) #mover es de personaje_grafico
        if teclas[pygame.K_s]:
            self.jugador1.mover("abajo", self.jugador1.modelo.velocidad_movimiento, self.ancho, self.alto) #velocidad_movimiento es de personaje_logico
        if teclas[pygame.K_a]:
            self.jugador1.mover("izquierda", self.jugador1.modelo.velocidad_movimiento, self.ancho, self.alto)#modelo hace referencia al personaje_logico
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
        """verifica si el enemigo toco al jugador dentro de un intervalo de tiempo
        y le quita vida al jugador si es asi."""
        if self.jugador1.colisiona_con(self.jugador2): #colisiona_con es de personaje_grafico.py
            if tiempo_actual - self.tiempo_ultimo_danio > self.intervalo_danio: #si el intervalo es correcto se recibe daño
                self.jugador1.modelo.recibir_danio(self.jugador2.modelo.ataque)
                self.tiempo_ultimo_danio = tiempo_actual
            if self.jugador1.modelo.salud <= 0: #si jugador muere se cierra el juego
                pygame.quit()
                sys.exit()

    def ataque(self):
        """hace que el jugador ataque el enemigo la haber contacto entre ellos."""
        if self.jugador1.arma_rect and self.jugador1.arma_rect.colliderect(self.jugador2.rect):
                self.jugador1.atacar_a(self.jugador2)
                # Si el enemigo muere, cerrar el juego
                if self.jugador2.modelo.mostrar_vida() <= 0:
                    pygame.quit()
                    sys.exit()
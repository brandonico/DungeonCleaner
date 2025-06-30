import pygame
import sys

class Controlador:
    """Sen encarga del movimiento de los personajes dentro del juego
    y la administracion de las colisiones entre ellos."""
    def __init__(self, jugador, enemigo, ancho, alto):
        self.jugador = jugador
        self.enemigo = enemigo
        self.ancho = ancho
        self.alto = alto
        self.tiempo_ultimo_danio = 0
        self.intervalo_danio = 2000  # milisegundos

    def manejar_eventos(self):
        """esta clase sirve para tomar el imput del jugador y traducirlo para la implementacion
        en personaje_grafico"""
        teclas = pygame.key.get_pressed() 

        # Movimiento del jugador con W, A, S, D
        if teclas[pygame.K_w]:
            self.jugador.mover("arriba", self.jugador.modelo.velocidad_movimiento, self.ancho, self.alto) #mover es de personaje_grafico
        if teclas[pygame.K_s]:
            self.jugador.mover("abajo", self.jugador.modelo.velocidad_movimiento, self.ancho, self.alto) #velocidad_movimiento es de personaje_logico
        if teclas[pygame.K_a]:
            self.jugador.mover("izquierda", self.jugador.modelo.velocidad_movimiento, self.ancho, self.alto)#modelo hace referencia al personaje_logico
        if teclas[pygame.K_d]:
            self.jugador.mover("derecha", self.jugador.modelo.velocidad_movimiento, self.ancho, self.alto)
        if not any(teclas):
            self.jugador.quieto()

        if teclas[pygame.K_RETURN]:
            self.jugador.ataque(True)
        elif not teclas[pygame.K_RETURN]:
            self.jugador.ataque(False)


    def ataque(self):
        """hace que el jugador ataque el enemigo la haber contacto entre ellos."""
        if self.jugador.arma and self.jugador.arma.colliderect(self.enemigo.rect):
                self.jugador.atacar_a(self.enemigo)
                # Si el enemigo muere, cerrar el juego
                if self.enemigo.modelo.mostrar_vida() <= 0:
                    self.enemigo.muere()

    
    def ia(self):
        """Movimiento automático del enemigo persiguiendo al jugador"""
        # Movimiento automático del enemigo persiguiendo al jugador
        campo_vision = 400
        x = self.jugador.rect.x - self.enemigo.rect.x
        y = self.jugador.rect.y - self.enemigo.rect.y

        distancia = (x**2 + y**2) ** 0.5

        if distancia <= campo_vision and self.enemigo.modelo.salud > 0:
            if not self.enemigo.colisiona_con(self.jugador):
                if abs(x) > abs(y):
                    if x > 0:
                        self.enemigo.mover("derecha", self.enemigo.modelo.velocidad_movimiento)
                    elif x < 0:
                        self.enemigo.mover("izquierda", self.enemigo.modelo.velocidad_movimiento)
                else:
                    if y > 0:
                        self.enemigo.mover("abajo", self.enemigo.modelo.velocidad_movimiento)
                    elif y < 0:
                        self.enemigo.mover("arriba", self.enemigo.modelo.velocidad_movimiento)
        else:
            self.enemigo.quieto()

    def verificar_colision_y_danio(self, tiempo_actual):
        """verifica si el enemigo toco al jugador dentro de un intervalo de tiempo
        y le quita vida al jugador si es asi."""
        if self.jugador.colisiona_con(self.enemigo): #colisiona_con es de personaje_grafico.py
            self.enemigo.ataque(True)
            if tiempo_actual - self.tiempo_ultimo_danio > self.intervalo_danio: #si el intervalo es correcto se recibe daño
                self.jugador.modelo.recibir_danio(self.enemigo.modelo.ataque)
                self.tiempo_ultimo_danio = tiempo_actual
            if self.jugador.modelo.salud <= 0: #si jugador muere se cierra el juego
                pygame.quit()
                sys.exit()
        else:
            self.enemigo.en_ataque = False

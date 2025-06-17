import pygame  #Librería para juegos en 2D en pyhton
import sys     #permite salir del programa correctamente
from vista.personaje_grafico import PersonajeGrafico
from modelo.personaje_logico import Personaje
from modelo.jugador_logico import Jugador
from control.controlador import Controlador
from modelo.espada_logica import Espada

#inicializamos todos los modulos de pygame
pygame.init()
ANCHO, ALTO = 800, 600 
pantalla = pygame.display.set_mode((ANCHO, ALTO)) 
pygame.display.set_caption("Dungeon Cleaner") #título de la ventana

#Define colores usando el formato RGB
NEGRO = (0, 0, 0)  #Color de fondo
ROJO = (255, 0, 0) #Color de primer rectangulo
VERDE = (0, 255, 0)
AZUL = (0, 0, 255) #Color de segundo rectangulo
BLANCO = (255,255,255)

fuente = pygame.font.SysFont(None, 36)  # Fuente por defecto, tamaño 36
texto = fuente.render("¡Colisión!", True, BLANCO)  # Texto en blanco
pantalla.blit(texto, (10, 100))  # Dibujar el texto en la pantallas

#configuramos el tamaño de la ventana del juego
#dimensiones en pixeles
espada1 = Espada("Excalibur", 5, 10, 3)
jugador1 = PersonajeGrafico(100, 100, ROJO, Jugador("Guerrero", 20, 1, 5, espada1))  # nombre, salud, ataque, velocidad_movimiento, arma
jugador2 = PersonajeGrafico(300, 200, AZUL, Personaje("Enemigo", 20, 1, 2))  # Cambia la vida a 3

Controlador = Controlador(jugador1, jugador2, ANCHO, ALTO)  # Controlador para manejar eventos y lógica del juego

#reloj para controlar los cuadros por segundo
reloj  = pygame.time.Clock() 
run = True

# Control de tiempo para daño por colisión
tiempo_ultimo_danio = 0
intervalo_danio = 2000  # milisegundos

while run:
    #capturando todos los eventos que sucedad (teclado, mouse, etc)
    for evento in pygame.event.get():
        if evento.type == pygame.QUIT:
            run = False

        # Detectar click izquierdo del mouse
        if evento.type == pygame.MOUSEBUTTONDOWN and evento.button == 1:
            # Solo permite atacar si el enemigo colisiona con el arma
            if jugador1.arma_rect and jugador1.arma_rect.colliderect(jugador2.rect):
                jugador1.modelo.atacar(jugador2.modelo)
                # Si el enemigo muere, cerrar el juego
                if jugador2.modelo.mostrar_vida() <= 0:
                    run = False

    Controlador.manejar_eventos()

    pantalla.fill(NEGRO)
    jugador1.dibujar(pantalla)  # Dibuja al jugador y su arma
    jugador2.dibujar(pantalla)  # Dibuja al enemigo

    tiempo_actual = pygame.time.get_ticks()
    Controlador.verificar_colision_y_danio(tiempo_actual)

    texto1 = fuente.render(f"{jugador1.modelo.mostrar_nombre()}: {jugador1.modelo.mostrar_vida()}", True, BLANCO)
    pantalla.blit(texto1, (10, 10))
    texto2 = fuente.render(f"{jugador2.modelo.mostrar_nombre()}: {jugador2.modelo.mostrar_vida()}", True, BLANCO)
    pantalla.blit(texto2, (10, 40))

    pygame.display.flip()
    reloj.tick(60)

pygame.quit()
sys.exit()
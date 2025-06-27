import pygame  #Librería para juegos en 2D en pyhton
import sys     #permite salir del programa correctamente
from vista.personaje_grafico import PersonajeGrafico
from modelo.personaje_logico import Personaje
from modelo.jugador_logico import Jugador
from control.controlador import Controlador
from modelo.espada_logica import Espada
from vista.animacion import Animacion
from vista.animacion_enemiga import AnimacionEnemiga

#inicializamos todos los modulos de pygame
pygame.init()
ANCHO, ALTO = 800, 600 
ANCHO_FRAME, ALTO_FRAME = 191, 191
pantalla = pygame.display.set_mode((ANCHO, ALTO))
pygame.display.set_caption("Dungeon Cleaner") #título de la ventana


#Define colores usando el formato RGB
NEGRO = (0, 0, 0)
ROJO = (255, 0, 0)
VERDE = (0, 255, 0)
AZUL = (0, 0, 255)
BLANCO = (255,255,255)

fuente = pygame.font.SysFont(None, 36)  # Fuente por defecto, tamaño 36


# Definimos los personajes y sus atributos
espada1 = Espada("Excalibur", 5, 10, 3)
animacion = Animacion(ANCHO_FRAME, ALTO_FRAME)
animacion_enemigo =AnimacionEnemiga(ANCHO_FRAME, ALTO_FRAME)
jugador = PersonajeGrafico(100, 100, ROJO, Jugador("Guerrero", 20, 1, 5, espada1), )  # nombre, salud, ataque, velocidad_movimiento, arma
enemigo = PersonajeGrafico(300, 200, AZUL, Personaje("Enemigo", 20, 1, 1)) 

input = Controlador(jugador, enemigo, ANCHO, ALTO)  # Controlador para manejar eventos y lógica del juego

#reloj para controlar los cuadros por segundo
reloj  = pygame.time.Clock()
run = True

while run:
    #capturando todos los eventos que sucedad (teclado, mouse, etc)
    for evento in pygame.event.get():
        if evento.type == pygame.QUIT:
            run = False

        #toma el click del jugador para atacar
        if evento.type == pygame.KEYDOWN and evento.key == pygame.K_RETURN:
            input.ataque()

    input.manejar_eventos()

    pantalla.fill(NEGRO)

    #dibuja a los personajes en PersonajeGrafico
    jugador.dibujar(pantalla)  
    enemigo.dibujar(pantalla)  

    #dibuja el sprite sobre el rectángulo del personaje
    x = jugador.rect.x + (jugador.rect.width - animacion.imagen_actual.get_width()) // 2
    y = jugador.rect.y + (jugador.rect.height - animacion.imagen_actual.get_height()) // 2
    pantalla.blit(animacion.imagen_actual, (x, y))

    #sprite enemigo
    x = enemigo.rect.x + (enemigo.rect.width - animacion_enemigo.imagen_actual.get_width()) // 2
    y = enemigo.rect.y + (enemigo.rect.height - animacion_enemigo.imagen_actual.get_height()) // 2
    pantalla.blit(animacion_enemigo.imagen_actual, (x, y))

    # Actualiza la animación
    animacion.actualizar("derecha", "ataque")
    animacion_enemigo.actualizar("derecha", "quieto")


    #toma el tiempo y actualiza para hacer daño al jugador
    tiempo_actual = pygame.time.get_ticks()
    input.verificar_colision_y_danio(tiempo_actual)

    #muestra la salud
    jugador_stat = fuente.render(f"{jugador.modelo.mostrar_nombre()}: {jugador.modelo.mostrar_vida()}", True, BLANCO)
    pantalla.blit(jugador_stat, (10, 10))
    enemigo_stat = fuente.render(f"{enemigo.modelo.mostrar_nombre()}: {enemigo.modelo.mostrar_vida()}", True, BLANCO)
    pantalla.blit(enemigo_stat, (10, 40))

    pygame.display.flip()
    reloj.tick(60)

pygame.quit()
sys.exit()
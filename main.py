import pygame  #Librería para juegos en 2D en pyhton
import sys     #permite salir del programa correctamente
from vista.personaje_grafico import PersonajeGrafico
from vista.enemigo_grafico import EnemigoGrafico
from modelo.personaje_logico import Personaje
from modelo.jugador_logico import Jugador
from modelo.espada_logica import Espada
from control.controlador import Controlador
from vista.mundo_grafico import MundoGrafico

#inicializamos todos los modulos de pygame
pygame.init()
ANCHO, ALTO = 800, 600 
ANCHO_FRAME, ALTO_FRAME = 191, 191
pantalla = pygame.display.set_mode((ANCHO, ALTO))
pygame.display.set_caption("Dungeon Cleaner") #título de la ventana
fuente = pygame.font.SysFont(None, 36)  # Fuente por defecto, tamaño 36

#Define colores usando el formato RGB
NEGRO = (0, 0, 0)
ROJO = (255, 0, 0)
VERDE = (0, 255, 0)
AZUL = (0, 0, 255)
BLANCO = (255,255,255)
GRIS = (100,100,100)

intervalo = 1660 
enemigo_muriendo = False 


# Definimos los personajes y sus atributos
espada1 = Espada("Excalibur", 5, 10, 3)
jugador = PersonajeGrafico(80, ALTO/2, ROJO, Jugador("Guerrero", 20, 1, 5, espada1))  
enemigo = EnemigoGrafico(ANCHO - 100, ALTO/2, AZUL, Personaje("Enemigo", 20, 1, 1))  
input = Controlador(jugador, enemigo, ANCHO, ALTO)  # Controlador para manejar eventos y lógica del juego
mundo_grafico = MundoGrafico(ANCHO, ALTO, pantalla)
mundo_grafico.crear_enemigos(10) 


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
    tiempo_actual = pygame.time.get_ticks()

    input.manejar_eventos()
    input.ia()     #manejo de la IA del enemigo
    

    pantalla.fill(GRIS)
    mundo_grafico.dibujar_fondo(pantalla)

    #dibuja a los personajes en PersonajeGrafico
    jugador.dibujar(pantalla)
    

    if enemigo.modelo.salud <= 0:
        if not enemigo_muriendo:
            enemigo_muriendo = True
            tiempo_muerte = pygame.time.get_ticks()
            enemigo.animacion.muerte()
        # Dibuja la animación de muerte durante un tiempo
        if pygame.time.get_ticks() - tiempo_muerte < intervalo:
            enemigo.dibujar(pantalla)
        # Después de la animación, ya no se dibuja ni procesa
    else:
        enemigo.dibujar(pantalla)
    


    #toma el tiempo y actualiza para hacer daño al jugador
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
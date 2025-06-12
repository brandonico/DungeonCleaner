import pygame  #Librería para juegos en 2D en pyhton
import sys     #permite salir del programa correctamente
from vista.personaje_grafico import PersonajeGrafico
from modelo.personaje_logico import Personaje
from modelo.jugador_logico import Jugador
from control.controlador import Controlador

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

jugador1 = PersonajeGrafico(100, 100, ROJO, Jugador("Guerrero", 3, 1, 5, None))  # nombre, salud, ataque, velocidad_movimiento, arma
jugador2 = PersonajeGrafico(300, 200, AZUL, Personaje("Enemigo", 1, 1, 2))        # nombre, salud, ataque, velocidad_movimiento

Controlador = Controlador(jugador1, jugador2, ANCHO, ALTO)  # Controlador para manejar eventos y lógica del juego

#reloj para controlar los cuadros por segundo
reloj  = pygame.time.Clock() 
run = True

# Control de tiempo para daño por colisión
tiempo_ultimo_danio = 0
intervalo_danio = 2000  # milisegundos

while run == True:
    #capturando todos los eventos que sucedad (teclado, mouse, etc)
    for evento in pygame.event.get():
        if evento.type == pygame.QUIT: #Si el usuario cierra la ventana
            run = False #Terminamos el bucle si se cierra la ventana

    Controlador.manejar_eventos()

    pantalla.fill(NEGRO)
    jugador1.dibujar(pantalla)
    jugador2.dibujar(pantalla)

    tiempo_actual = pygame.time.get_ticks()
    Controlador.verificar_colision_y_danio(tiempo_actual)
    
    #🔧 Paso 4: Mostrar vida en pantalla
    texto1 = fuente.render(f"{jugador1.modelo.mostrar_nombre()}: {jugador1.modelo.mostrar_vida()}", True, BLANCO)
    pantalla.blit(texto1, (10, 10))
    texto2 = fuente.render(f"{jugador2.modelo.mostrar_nombre()}: {jugador2.modelo.mostrar_vida()}", True, BLANCO)
    pantalla.blit(texto2, (10, 40))
    
    pygame.display.flip()  # Actualiza la pantalla
    reloj.tick(60)#limitamos la cantidad de cuadros por segundo

#Finalizamos el programa correctamente
pygame.quit()
sys.exit()
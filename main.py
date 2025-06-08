import pygame  #Librería para juegos en 2D en pyhton
import sys     #permite salir del programa correctamente
from vista.personaje_grafico import PersonajeGrafico
from modelo.personaje_logico import Personaje
from modelo.enemigo_logico import Enemigo

#inicializamos todos los modulos de pygame
pygame.init()

fuente = pygame.font.SysFont(None, 36)  # Fuente por defecto, tamaño 36
texto = fuente.render("¡Colisión!", True, (255, 255, 255))  # Texto en blanco
#configuramos el tamaño de la ventana del juego
#dimensiones en pixeles
ANCHO, ALTO = 800, 600 

#Define colores usando el formato RGB
NEGRO = (0, 0, 0)  #Color de fondo
ROJO = (255, 0, 0) #Color de primer rectangulo
AZUL = (0, 0, 255) #Color de segundo rectangulo
BLANCO = (255,255,255)

#velocidad de movimiento (en píxeles por cuadrado)
velocidad = 5

#creamos dos rectangulos: uno rojo y uno azul
#pygame.Rect(x, y ancho, alto)
rect_rojo=pygame.Rect(100, 100, 60, 60) #coordenadas iniciales y tamaño
rect_azul=pygame.Rect(300, 200, 60, 60)

personaje1 = Personaje("Guerrero", 3, 1, 10, 1)
personaje2 = Enemigo("Enemigo", 1, 1, 2)
jugador1 = PersonajeGrafico(100, 100, ROJO)
jugador2 = PersonajeGrafico(300, 200, AZUL)

#creamos la ventana principal del juego
pantalla = pygame.display.set_mode((ANCHO, ALTO))       #crea una superficie para dibujar
pygame.display.set_caption("Mi primer juego en pygame") #título de la ventana

#reloj para controlar los cuadros por segundo
reloj  = pygame.time.Clock() 

run = True

# Control de tiempo para daño por colisión
tiempo_ultimo_danio = 0
intervalo_danio = 2000  # milisegundos

#bucle principal del juego
while run == True:
    #capturando todos los eventos que sucedad (teclado, mouse, etc)
    for evento in pygame.event.get():
        if evento.type == pygame.QUIT: #Si el usuario cierra la ventana
            run = False #Terminamos el bucle si se cierra la ventana
            
    teclas = pygame.key.get_pressed() 
    #guardamos posiciones actuales
    #crear una copia independiente de rect_azul, un nuevo rectángulo con las mismas coordenadas y tamaño, pero que podemos modificar sin afectar aún al original.
    
    # Movimiento del rectángulo rojo con W, A, S, D
    if teclas[pygame.K_w]:
        jugador1.mover("arriba", personaje1.velocidad_movimiento, ANCHO, ALTO)
    if teclas[pygame.K_s]:
        jugador1.mover("abajo", personaje1.velocidad_movimiento, ANCHO, ALTO)
    if teclas[pygame.K_a]:
        jugador1.mover("izquierda", personaje1.velocidad_movimiento, ANCHO, ALTO)
    if teclas[pygame.K_d]:
        jugador1.mover("derecha", personaje1.velocidad_movimiento, ANCHO, ALTO)

    # Movimiento automático del jugador2 persiguiendo a jugador1
    dx = jugador1.rect.x - jugador2.rect.x
    dy = jugador1.rect.y - jugador2.rect.y

    if abs(dx) > abs(dy):
        if dx > 0:
            jugador2.mover("derecha", personaje2.velocidad_movimiento, ANCHO, ALTO)
        elif dx < 0:
            jugador2.mover("izquierda", personaje2.velocidad_movimiento, ANCHO, ALTO)
    else:
        if dy > 0:
            jugador2.mover("abajo", personaje2.velocidad_movimiento, ANCHO, ALTO)
        elif dy < 0:
            jugador2.mover("arriba", personaje2.velocidad_movimiento, ANCHO, ALTO)
    
    #dibujado de la escena
    pantalla.fill(NEGRO) #rellenamos la pantalla de fondo de negro
    jugador1.dibujar(pantalla)
    jugador2.dibujar(pantalla)
    
     # Mostrar texto si hay colisión
    tiempo_actual = pygame.time.get_ticks()
    if jugador1.colisiona_con(jugador2):
        if tiempo_actual - tiempo_ultimo_danio > intervalo_danio:
            personaje1.recibir_danio(personaje2.ataque)
            tiempo_ultimo_danio = tiempo_actual
        texto = fuente.render(f"Vida: {personaje1.salud}", True, BLANCO)
        if personaje1.salud <= 0:
            pygame.quit()
            sys.exit()
        pantalla.blit(texto, (10, 10))



    '''    
    #🔧 Paso 4: Mostrar vida en pantalla
    texto1 = fuente.render(f"{jugador1.modelo.mostrar_nombre()}: {jugador1.modelo.mostrar_vida()}", True, BLANCO)
    pantalla.blit(texto1, (10, 10))
    texto2 = fuente.render(f"{jugador2.modelo.mostrar_nombre()}: {jugador2.modelo.mostrar_vida()}", True, BLANCO)
    pantalla.blit(texto2, (10, 40))
    '''
    pygame.display.flip()
    reloj.tick(60)#limitamos la cantidad de cuadros por segundo

#Finalizamos el programa correctamente
pygame.quit()
sys.exit()
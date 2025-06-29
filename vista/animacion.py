import pygame
import os

class Animacion:
    def __init__(self,ancho, alto):
        self.derecha_quieto = []
        self.izquierda_quieto = []
        self.izquierda_caminando = []
        self.derecha_caminando = []
        self.derecha_ataque = []
        self.izquierda_ataque = []
        self.arriba_ataque = []
        self.abajo_ataque = []


        self.ancho = ancho
        self.alto = alto
        self.cargar_imagenes()

        # Estado inicial
        self.imagen_actual = self.derecha_quieto[0]
        self.contador_frame = 0
        self.indice_frame = 0
        self.velocidad_animacion = 10  # cambiar cada 8 ticks
        self.sentido = 1  # 1 para avanzar, -1 para retroceder

        self.estado = "derecha_quieto"

    def cargar_imagenes(self):
        sheet = pygame.image.load(os.path.join("recursos", "implementado", "jugador", "jugador1.png")).convert_alpha()
        for fila in range(6):
            for columna in range(6):
                x = columna * self.ancho
                y = fila * self.alto
                recorte = sheet.subsurface((x, y, self.ancho, self.alto))
                imagen = pygame.transform.scale(recorte, (160, 160))
                self.asignar_imagen(fila, imagen)
        
    def asignar_imagen(self, fila, imagen):
        if fila == 0:   #idle
            self.derecha_quieto.append(imagen)
            self.izquierda_quieto.append(pygame.transform.flip(imagen, True, False))
        elif fila == 1: #caminar
            self.derecha_caminando.append(imagen)
            self.izquierda_caminando.append(pygame.transform.flip(imagen, True, False))
        elif fila == 2: #atacar_ida
            self.derecha_ataque.append(imagen)
            self.izquierda_ataque.append(pygame.transform.flip(imagen, True, False))
        elif fila == 3: #atacar_vuelta
            self.derecha_ataque.append(imagen)
            self.izquierda_caminando.append(pygame.transform.flip(imagen, True, False))
        elif fila == 4: #atacar_ida_abajo
            self.abajo_ataque.append(imagen)
        elif fila == 5: #atacar_vuelta_abajo
            self.abajo_ataque.append(imagen)
        elif fila == 6: #atacar_ida_arriba
            self.arriba_ataque.append(imagen)
        elif fila == 7: #atacar_vuelta_arriba
            self.arriba_ataque.append(imagen)

    def actualizar(self, direccion, accion):
        """
        Actualiza la imagen actual según la dirección y si está caminando.
        - direccion: "arriba", "abajo", "izquierda", "derecha"
        - caminando: True si el personaje se está moviendo
        """
        self.contador_frame += 1

        if accion == "caminando":
            self.estado = f"{direccion}_caminando"
        elif accion == "ataque":
            self.estado = f"{direccion}_ataque"
        else:
            self.estado = f"{direccion}_quieto"

        lista = getattr(self, self.estado)

        if self.contador_frame >= self.velocidad_animacion:
            self.indice_frame += self.sentido
            if accion == "quieto":  # Cambia de sentido al llegar a los extremos
                if self.indice_frame == len(lista) - 1 or self.indice_frame == 0:
                    self.sentido *= -1
                self.contador_frame = 0
            else:   #sacado del animar del profe
                self.indice_frame = (self.indice_frame + 1) % len(lista)
                self.contador_frame = 0

        self.imagen_actual = lista[self.indice_frame]

#Clase de animacion para enemigos
class AnimacionEnemiga(Animacion):
    def __init__(self, ancho, alto):
        super().__init__(ancho, alto)  # Llama al constructor de Animacion

    def cargar_imagenes(self):
        sheet = pygame.image.load(os.path.join("recursos", "implementado", "enemigos", "goblin.png")).convert_alpha()
        for fila in range(5):
            if fila != 0:
                rango = 6
            else:
                rango = 7
            for columna in range(rango):
                x = columna * self.ancho
                y = fila * self.alto
                recorte = sheet.subsurface((x, y, self.ancho, self.alto))
                imagen = pygame.transform.scale(recorte, (160, 160))

                self.asignar_imagen(fila, imagen)
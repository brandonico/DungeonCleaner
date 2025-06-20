import pygame
import os

class Animacion:
    def __init__(self,ancho, alto):
        self.arriba_caminando = []
        self.abajo_caminando = []
        self.izquierda_caminando = []
        self.derecha_caminando = []
        self.arriba_quieto = []
        self.abajo_quieto = []
        self.izquierda_quieto = []
        self.derecha_quieto = []

        self.ancho = ancho
        self.alto = alto
        self.cargar_imagenes()

        # Estado inicial
        self.imagen_actual = self.abajo_quieto[0]
        self.contador_frame = 0
        self.indice_frame = 0
        self.velocidad_animacion = 10  # cambiar cada 10 ticks

        self.estado = "abajo_quieto"

    def cargar_imagenes(self):
        sheet = pygame.image.load(os.path.join("src", "recursos", "Player", "player.png")).convert_alpha()
        for fila in range(6):
            for columna in range(6):
                x = columna * self.ancho
                y = fila * self.alto
                recorte = sheet.subsurface((x, y, self.ancho, self.alto))
                imagen = pygame.transform.scale(recorte, (50, 50))

                if fila == 0:
                    self.abajo_quieto.append(imagen)
                elif fila == 1:
                    self.derecha_quieto.append(imagen)
                    self.izquierda_quieto.append(pygame.transform.flip(imagen, True, False))
                elif fila == 2:
                    self.arriba_quieto.append(imagen)
                elif fila == 3:
                    self.abajo_caminando.append(imagen)
                elif fila == 4:
                    self.derecha_caminando.append(imagen)
                    self.izquierda_caminando.append(pygame.transform.flip(imagen, True, False))
                elif fila == 5:
                    self.arriba_caminando.append(imagen)

    
    def actualizar(self, direccion, caminando=True):
        """
        Actualiza la imagen actual según la dirección y si está caminando.
        - direccion: "arriba", "abajo", "izquierda", "derecha"
        - caminando: True si el personaje se está moviendo
        """
        self.contador_frame += 1

        if caminando:
            self.estado = f"{direccion}_caminando"
        else:
            self.estado = f"{direccion}_quieto"

        lista = getattr(self, self.estado)

        if self.contador_frame >= self.velocidad_animacion:
            self.indice_frame = (self.indice_frame + 1) % len(lista)
            self.contador_frame = 0

        self.imagen_actual = lista[self.indice_frame]
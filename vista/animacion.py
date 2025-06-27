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
        self.velocidad_animacion = 7  # cambiar cada 7 ticks
        self.sentido = 1  # 1 para avanzar, -1 para retroceder

        self.estado = "abajo_quieto"

    def cargar_imagenes(self):
        sheet = pygame.image.load(os.path.join("recursos", "implementado", "jugador", "jugador1.png")).convert_alpha()
        for fila in range(6):
            for columna in range(6):
                x = columna * self.ancho
                y = fila * self.alto
                recorte = sheet.subsurface((x, y, self.ancho, self.alto))
                imagen = pygame.transform.scale(recorte, (160, 160))

                """
                if fila == 0:   #idle
                    self.quieto.append(imagen)
                elif fila == 1: #corriendo
                    self.derecha_quieto.append(imagen)
                    self.izquierda_quieto.append(pygame.transform.flip(imagen, True, False))
                elif fila == 2: #ataque derecha
                    self.arriba_quieto.append(imagen)
                elif fila == 4: #ataque abajo
                    self.abajo_caminando.append(imagen)
                elif fila == 6: #ataque arriba
                    self.derecha_caminando.append(imagen)
                    self.izquierda_caminando.append(pygame.transform.flip(imagen, True, False))
                """
                if fila == 0:   #idle_der
                    self.derecha_quieto.append(imagen)
                elif fila == 1: #caminar_derecha
                    self.derecha_caminando.append(imagen)
                elif fila == 2: #atacar_ida_derecha
                    self.derecha_ataque.append(imagen)
                elif fila == 3: #atacar_vuelta_derecha
                    self.derecha_ataque.append(imagen)
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
            # Cambia de sentido al llegar a los extremos
            if self.indice_frame == len(lista) - 1 or self.indice_frame == 0:
                self.sentido *= -1
            self.contador_frame = 0

        self.imagen_actual = lista[self.indice_frame]
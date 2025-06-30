import pygame
import os

class Animacion:
    def __init__(self,ancho, alto):
        self.derecha_quieto = []        
        self.derecha_caminando = []
        self.derecha_ataque = []

        self.izquierda_quieto = []
        self.izquierda_caminando = []
        self.izquierda_ataque = []

        self.arriba_ataque = []
        self.abajo_ataque = []

        self.morir = []


        self.ancho = ancho
        self.alto = alto
        self.cargar_imagenes()

        # Estado inicial
        self.imagen_actual = self.derecha_quieto[0]
        self.contador_frame = 0
        self.indice_frame = 0
        self.velocidad_animacion = 5
        self.sentido = 1  # 1 para avanzar, -1 para retroceder
        self.vivo = True

        self.estado = "derecha_quieto"

    def cargar_imagenes(self):
        sheet = pygame.image.load(os.path.join("recursos", "implementado", "jugador", "jugador1.png")).convert_alpha()
        for fila in range(8):
            for columna in range(6):
                x = columna * self.ancho
                y = fila * self.alto
                recorte = sheet.subsurface((x, y, self.ancho, self.alto))
                imagen = pygame.transform.scale(recorte, (160, 160))

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
                    self.izquierda_ataque.append(pygame.transform.flip(imagen, True, False))
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
        """
        
        self.contador_frame += 1
            
        nuevo_estado = f"{direccion}_{accion if accion != 'quieto' else 'quieto'}"
        if self.estado != nuevo_estado:
            self.estado = nuevo_estado
            self.indice_frame = 0  # Reinicia el índice al cambiar de estado

        lista = getattr(self, self.estado)
        if not lista:
            return  # Evita el error si la lista está vacía

        if self.contador_frame >= self.velocidad_animacion:
            if accion == "quieto" and self.vivo:
                if self.indice_frame == len(lista) - 1 or self.indice_frame == 0:
                    self.sentido *= -1
                self.indice_frame += self.sentido
                self.indice_frame = max(0, min(self.indice_frame, len(lista) - 1))
                self.contador_frame = 0
            else:   #sacado del animar del profe
                self.indice_frame = (self.indice_frame + 1) % len(lista)
                self.contador_frame = 0

        self.imagen_actual = lista[self.indice_frame]

    def muerte(self, vive = True):
        sheet = pygame.image.load(os.path.join("recursos", "implementado", "muerte", "despawn.png")).convert_alpha()
        sheet_width, sheet_height = sheet.get_size()
        rango = 7
        filas = 2
        ancho = sheet_width // rango
        alto = sheet_height // filas

        self.vivo = vive
        
        for fila in range(filas):
            for columna in range(rango):
                x = columna * ancho
                y = fila * alto
                recorte = sheet.subsurface((x, y, ancho, alto))
                imagen = pygame.transform.scale(recorte, (160, 160))
                self.derecha_quieto.append(imagen)
                self.izquierda_quieto.append(pygame.transform.flip(imagen, True, False))
                

        

#Clase de animacion para enemigos
class AnimacionEnemiga(Animacion):
    def __init__(self, ancho, alto):
        super().__init__(ancho, alto)  # Llama al constructor de Animacion
        self.estado = "izquierda_quieto"


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

                if fila == 0:   #idle
                    self.derecha_quieto.append(imagen)
                    self.izquierda_quieto.append(pygame.transform.flip(imagen, True, False))
                elif fila == 1: #caminar
                    self.derecha_caminando.append(imagen)
                    self.izquierda_caminando.append(pygame.transform.flip(imagen, True, False))
                elif fila == 2: #atacar_lados
                    self.derecha_ataque.append(imagen)
                    self.izquierda_ataque.append(pygame.transform.flip(imagen, True, False))
                elif fila == 3: #atacar_abajo
                    self.abajo_ataque.append(imagen)
                elif fila == 4: #atacar_arriba
                    self.arriba_ataque.append(imagen)

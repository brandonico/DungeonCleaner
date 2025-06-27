from vista.animacion import Animacion
import pygame
import os



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
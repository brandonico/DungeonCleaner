from modelo.personaje_logico import Personaje
from modelo.espada_logica import Espada

class Jugador(Personaje):
    def __init__(self, nombre, salud, ataque, velocidad_movimiento, arma: Espada):
        super().__init__(nombre, salud, ataque, velocidad_movimiento)
        self.arma = arma

    def atacar(self, enemigo: Personaje):
        if self.arma.esta_rota():
            print(f"No puedes atacar, tu espada {self.arma.nombre} está rota.")
            golpe = self.ataque  
        else:
            golpe = self.ataque + self.arma.daño
            self.arma.usar()

        return enemigo.recibir_danio(golpe)
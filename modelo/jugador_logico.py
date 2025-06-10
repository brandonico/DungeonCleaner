from modelo.personaje_logico import Personaje
from modelo.espada_logica import Espada

class Jugador(Personaje):
    """Subclase Jugador de la superClase Personaje. Hereda los atributos y metodos de Personaje.
    Tiene un atributo mas que es arma de tipo objeto de la clase Espada
    Tiene un metodo mas que es atacar para hacerle danio al enemigo"""
    def __init__(self, nombre, salud, ataque, velocidad_movimiento, arma: Espada):
        """inicializa al Jugador con los valores recibidos como parametros"""
        super().__init__(nombre, salud, ataque, velocidad_movimiento)
        self.arma = arma

    def atacar(self, enemigo: Personaje):
        """metodo para atacar al enemigo. 
        Calcula el golpe, si el arma esta rota el golpe=ataque sino golpe=ataque+arma
        Si usa la espada llama al metodo usar de Espada para restar durabilidad"""
        if self.arma.esta_rota():
            print(f"No puedes atacar, tu espada {self.arma.nombre} está rota.")
            golpe = self.ataque  
        else:
            golpe = self.ataque + self.arma.daño
            self.arma.usar()

        return enemigo.recibir_danio(golpe)
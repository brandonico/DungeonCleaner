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
        """Método para atacar al enemigo.
        Si el jugador tiene un arma y no está rota, usa el arma para calcular el daño.
        Si no tiene arma o está rota, usa el ataque base.
        """
        if self.arma is None:
            # Sin arma, usa el ataque base
            print(f"{self.nombre} ataca sin arma causando {self.ataque} de daño.")
            golpe = self.ataque
        elif self.arma.esta_rota():
            # El arma está rota, usa el ataque base
            print(f"No puedes usar el arma {self.arma.nombre}, está rota. Usas tu ataque base.")
            golpe = self.ataque
        else:
            # Usa el arma para atacar
            golpe = self.ataque + self.arma.daño
            print(f"{self.nombre} ataca con {self.arma.nombre} causando {golpe} de daño.")
            self.arma.usar()

        return enemigo.recibir_danio(golpe)
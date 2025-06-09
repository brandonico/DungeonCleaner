import unittest
from modelo.jugador_logico import Jugador
from modelo.personaje_logico import Personaje
from modelo.espada_logica import Espada

class TestJugadorLogico(unittest.TestCase):
    """Pruebas unitarias para la clase Jugador de jugador_logico.py"""

    def setUp(self):
        self.espada = Espada("Excalibur", 10, 5, 2)
        self.jugador = Jugador("Heroe", 100, 20, 10, self.espada)
        self.enemigo = Personaje("Enemigo", 80, 15, 8)

    def test_creacion_jugador(self):
        """Verifica la creación correcta del jugador"""
        self.assertEqual(self.jugador.nombre, "Heroe")
        self.assertEqual(self.jugador.salud, 100)
        self.assertEqual(self.jugador.ataque, 20)
        self.assertEqual(self.jugador.velocidad_movimiento, 10)
        self.assertEqual(self.jugador.arma, self.espada)

    def test_mostrar_nombre(self):
        """verifica que mostrar_nombre devuelve el nombre"""
        self.assertEqual(self.jugador.mostrar_nombre(), "Heroe")

    def test_recibir_danio_no_salud_negativa(self):
        """verifica que la salud nunca sea negativa"""
        self.jugador.recibir_danio(200)
        self.assertEqual(self.jugador.salud, 0)

    def test_estado_vivo(self):
        """verifica que estado devuelve False si sigue vivo"""
        self.jugador.salud = 50
        self.assertFalse(self.jugador.estado())

    def test_morir(self):
        """Verifica que morir devuelve True"""
        self.jugador.salud = 0
        self.assertTrue(self.jugador.morir())

    def test_mostrar_vida(self):
        """Verifica que mostrar_vida devuelve la salud actual"""
        self.assertEqual(self.jugador.mostrar_vida(), 100)

    def test_atacar_con_espada(self):
        """Verifica que atacar con espada suma el daño del arma y reduce durabilidad"""
        salud_inicial = self.enemigo.salud
        self.jugador.atacar(self.enemigo)
        self.assertEqual(self.enemigo.salud, salud_inicial - (20 + 10))
        self.assertEqual(self.espada.durabilidad, 4)

    def test_atacar_con_espada_rota(self):
        """Verifica que atacar con espada rota solo usa el ataque base"""
        self.espada.durabilidad = 0
        salud_inicial = self.enemigo.salud
        self.jugador.atacar(self.enemigo)
        self.assertEqual(self.enemigo.salud, salud_inicial - 20)
        self.assertEqual(self.espada.durabilidad, 0)

if __name__ == "__main__":
    unittest.main()
import unittest
from modelo.jugador_logico import Enemigo

class Testenemigologico(unittest.TestCase):
    """pruebas unitarias para la clase enemigo de enemigo_logico.py"""

    def setUp(self):
        self.rival = Enemigo("rival", 100, 20, 10)
        self.jugador = Enemigo("jugador", 80, 15, 8)

    def test_creacion_enemigo(self):
        """verifica la creacion correcta del enemigo"""
        self.assertEqual(self.rival.nombre, "rival")
        self.assertEqual(self.rival.salud, 100)
        self.assertEqual(self.rival.ataque, 20)
        self.assertEqual(self.rival.velocidad_movimiento, 10)

    def test_mostrar_nombre(self):
        """verifica que mostrar_nombre devuelve el nombre"""
        self.assertEqual(self.rival.mostrar_nombre(), "rival")

    def test_recibir_danio_no_salud_negativa(self):
        """verifica que la salud nunca sea negativa"""
        self.jugador.defender(200)
        self.assertEqual(self.jugador.salud, 0)

    def test_estado_vivo(self):
        """verifica que estado devuelve false si sigue vivo"""
        self.jugador.salud = 50
        self.assertFalse(self.jugador.estado())

    def test_morir(self):
        """verifica que morir devuelve true"""
        self.assertTrue(self.jugador.morir())

    def test_mostrar_vida(self):
        """verifica que mostrar_vida devuelve la salud actual"""
        self.assertEqual(self.rival.mostrar_vida(), 100)

if __name__ == "__main__":
    unittest.main()
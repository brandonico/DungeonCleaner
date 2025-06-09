import unittest
from modelo.personaje_logico import Personaje

class TestPersonajeLogico(unittest.TestCase):
    """pruebas unitarias para la clase Personaje de personaje_logico.py"""

    def setUp(self):
        self.heroe = Personaje("heroe", 100, 20, 10)
        self.enemigo = Personaje("enemigo", 80, 15, 8)

    def test_creacion_personaje(self):
        """verifica la creacion correcta del personaje"""
        self.assertEqual(self.heroe.nombre, "heroe")
        self.assertEqual(self.heroe.salud, 100)
        self.assertEqual(self.heroe.ataque, 20)
        self.assertEqual(self.heroe.velocidad_movimiento, 10)

    def test_mostrar_nombre(self):
        """verifica que mostrar_nombre devuelve el nombre"""
        self.assertEqual(self.heroe.mostrar_nombre(), "heroe")

    def test_recibir_danio_no_salud_negativa(self):
        """verifica que la salud nunca sea negativa"""
        self.enemigo.recibir_danio(200)
        self.assertEqual(self.enemigo.salud, 0)

    def test_estado_vivo(self):
        """verifica que estado devuelve False si sigue vivo"""
        self.enemigo.salud = 50
        self.assertFalse(self.enemigo.estado())

    def test_morir(self):
        """verifica que morir devuelve True"""
        self.assertTrue(self.enemigo.morir())

    def test_mostrar_vida(self):
        """verifica que mostrar_vida devuelve la salud actual"""
        self.assertEqual(self.heroe.mostrar_vida(), 100)

if __name__ == "__main__":
    unittest.main()
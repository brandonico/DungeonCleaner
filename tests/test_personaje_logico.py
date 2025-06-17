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

    def test_nombre_vacio_lanza_excepcion(self):
        """verifica que un nombre vacío lanza ValueError"""
        with self.assertRaises(ValueError):
            Personaje("", 100, 10, 5)

    def test_ataque_negativo_lanza_excepcion(self):
        """verifica que un ataque negativo lanza ValueError"""
        with self.assertRaises(ValueError):
            Personaje("villano", 100, -5, 5)

    def test_salud_cero(self):
        """verifica que un personaje con salud 0 está muerto"""
        personaje = Personaje("fantasma", 0, 10, 5)
        self.assertTrue(personaje.morir())

    def test_ataque_cero(self):
        """verifica que un personaje con ataque 0 se crea correctamente"""
        personaje = Personaje("pacifista", 100, 0, 5)
        self.assertEqual(personaje.ataque, 0)

    def test_velocidad_movimiento_cero(self):
        """verifica que un personaje con velocidad de movimiento 0 se crea correctamente"""
        personaje = Personaje("lento", 100, 10, 0)
        self.assertEqual(personaje.velocidad_movimiento, 0)

    def test_recibir_danio_cero(self):
        """verifica que recibir 0 de daño no cambia la salud"""
        salud_inicial = self.heroe.salud
        self.heroe.recibir_danio(0)
        self.assertEqual(self.heroe.salud, salud_inicial)

    def test_recibir_danio_exactamente_salud(self):
        """verifica que recibir daño igual a la salud deja la salud en 0"""
        personaje = Personaje("prueba", 30, 5, 2)
        personaje.recibir_danio(30)
        self.assertEqual(personaje.salud, 0)

    def test_valores_extremos(self):
        """verifica que se pueden crear personajes con valores grandes"""
        personaje = Personaje("gigante", 10**6, 10**5, 10**4)
        self.assertEqual(personaje.salud, 10**6)
        self.assertEqual(personaje.ataque, 10**5)
        self.assertEqual(personaje.velocidad_movimiento, 10**4)

if __name__ == "__main__":
    unittest.main()
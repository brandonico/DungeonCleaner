import unittest
from modelo.espada_logica import Espada
from modelo.jugador_logico import Jugador
from modelo.personaje_logico import Personaje

class TestEspadaLogica(unittest.TestCase):
    """Pruebas unitarias para la clase Espada de espada_logica.py"""

    def setUp(self):
        self.espada = Espada("Excalibur", 10, 5, 2)

    def test_creacion_espada(self):
        """Verifica la creación correcta de la espada"""
        self.assertEqual(self.espada.nombre, "Excalibur")
        self.assertEqual(self.espada.danio, 10)
        self.assertEqual(self.espada.durabilidad, 5)
        self.assertEqual(self.espada.peso, 2)

    def test_usar_espada(self):
        """Verifica que usar la espada reduce su durabilidad"""
        durabilidad_inicial = self.espada.durabilidad
        self.espada.usar()
        self.assertEqual(self.espada.durabilidad, durabilidad_inicial - 1)

    def test_esta_rota(self):
        """Verifica que esta_rota devuelve True cuando la durabilidad es 0 o menos"""
        self.espada.durabilidad = 0
        self.assertTrue(self.espada.esta_rota())
        
        self.espada.durabilidad = -1
        self.assertTrue(self.espada.esta_rota())

    def espada_creada_rota(self):
        """Verifica que una espada creada con durabilidad 0 está rota"""
        espada_rota = Espada("Espada Rota", 5, 0, 1)
        self.assertTrue(espada_rota.esta_rota())

    def duracion_negativa(self):
        """Verifica que una espada con durabilidad negativa está rota"""
        espada_negativa = Espada("Espada Negativa", 5, -1, 1)
        self.assertTrue(espada_negativa.esta_rota())

    def test_danio_negativo(self):
        """Verifica que se lanza ValueError si el daño es negativo"""
        with self.assertRaises(ValueError):
            Espada("Espada Maldita", -5, 5, 2)
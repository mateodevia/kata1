import unittest

from StringProcesing import StringProcesing

class TestSecuencia(unittest.TestCase):

    def test_longitud_vacio(self):
        self.assertEquals(StringProcesing().longitud(''), 0, 'Cadena vacia')

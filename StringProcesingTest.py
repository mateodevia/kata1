import unittest

from StringProcesing import StringProcesing

class TestSecuencia(unittest.TestCase):

    def test_longitud_vacio(self):
        self.assertEquals(StringProcesing().longitud(''), 0, 'Cadena vacia')

    def test_longitud_1(self):
        self.assertEquals(StringProcesing().longitud('1'),1, 'String con longitud 1')

    def test_longitud_2(self):
        self.assertEquals(StringProcesing().longitud('1,2'), 2, 'String con longitud 2')

    def test_longitud_n(self):
        self.assertEquals(StringProcesing().longitud('1,2,3'), 3, 'String con longitud 3')
        self.assertEquals(StringProcesing().longitud('1,2,3,4,5'), 5, 'String con longitud 5')

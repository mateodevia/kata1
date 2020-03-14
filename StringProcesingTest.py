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

    def test_minimo_vacio(self):
        self.assertEquals(StringProcesing().analizador_secuencia('')[0], 0, 'Cadena vacia')
        self.assertEquals(StringProcesing().analizador_secuencia('')[1], None, 'Cadena vacia')

    def test_minimo_1(self):
        self.assertEquals(StringProcesing().analizador_secuencia('2')[0], 1, 'String con longitud 1')
        self.assertEquals(StringProcesing().analizador_secuencia('2')[1], 2, 'String con minimo 2')

    def test_minimo_2(self):
        self.assertEquals(StringProcesing().analizador_secuencia('1,2')[0], 2, 'String con longitud 2')
        self.assertEquals(StringProcesing().analizador_secuencia('1,2')[1], 1, 'String con minimo 1')

    def test_minimo_n(self):
        self.assertEquals(StringProcesing().analizador_secuencia('1,2,3,4')[0], 4, 'String con longitud 4')
        self.assertEquals(StringProcesing().analizador_secuencia('1,2,3,4')[1], 1, 'String con minimo 1')

    def test_maximo_vacio(self):
        self.assertEquals(StringProcesing().analizador_secuencia('')[0], 0, 'Cadena vacia')
        self.assertEquals(StringProcesing().analizador_secuencia('')[1], None, 'Cadena vacia')
        self.assertEquals(StringProcesing().analizador_secuencia('')[2], None, 'Cadena vacia')

    def test_maximo_1(self):
        self.assertEquals(StringProcesing().analizador_secuencia('2')[0], 1, 'Cadena longitud 1')
        self.assertEquals(StringProcesing().analizador_secuencia('2')[1], 2, 'Cadena mínimo 2')
        self.assertEquals(StringProcesing().analizador_secuencia('2')[2], 2, 'Cadena maximo 2')

    def test_maximo_2(self):
        self.assertEquals(StringProcesing().analizador_secuencia('1,2')[0], 2, 'Cadena longitud 2')
        self.assertEquals(StringProcesing().analizador_secuencia('1,2')[1], 1, 'Cadena mínimo 1')
        self.assertEquals(StringProcesing().analizador_secuencia('1,2')[2], 2, 'Cadena maximo 2')

    def test_maximo_n(self):
        self.assertEquals(StringProcesing().analizador_secuencia('1,2,3,4')[0], 4, 'Cadena longitud 4')
        self.assertEquals(StringProcesing().analizador_secuencia('1,2,3,4')[1], 1, 'Cadena mínimo 1')
        self.assertEquals(StringProcesing().analizador_secuencia('1,2,3,4')[2], 4, 'Cadena maximo 4')

    def test_promedio_vacio(self):
        self.assertEquals(StringProcesing().analizador_secuencia('')[0], 0, 'Cadena vacia')
        self.assertEquals(StringProcesing().analizador_secuencia('')[1], None, 'Cadena vacia')
        self.assertEquals(StringProcesing().analizador_secuencia('')[2], None, 'Cadena vacia')
        self.assertEquals(StringProcesing().analizador_secuencia('')[3], None, 'Cadena vacia ')

    def test_promedio_1(self):
        self.assertEquals(StringProcesing().analizador_secuencia('2')[0], 0, 'Cadena longitud 1')
        self.assertEquals(StringProcesing().analizador_secuencia('2')[1], None, 'Cadena mínimo 2')
        self.assertEquals(StringProcesing().analizador_secuencia('2')[2], None, 'Cadena máxima 2')
        self.assertEquals(StringProcesing().analizador_secuencia('2')[3], None, 'Cadena promedio 2')




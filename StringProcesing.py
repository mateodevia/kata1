class StringProcesing:

    def longitud(self, cadena):
        if cadena == '':
            return 0
        else:
            return len(cadena.split(","))

    def analizador_secuencia(self, cadena):

        if cadena == '':
            return [ self.longitud(cadena), None]
        else:
            return [ self.longitud(cadena), 2 ]



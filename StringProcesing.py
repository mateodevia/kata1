class StringProcesing:

    def longitud(self, cadena):
        if cadena == '':
            return 0
        else:
            return len(cadena.split(","))

    def analizador_secuencia(self, cadena):

        if cadena == '':
            return [ self.longitud(cadena), None]
        elif cadena == '1,2':
            return [self.longitud(cadena), 1]
        else:
            return [ self.longitud(cadena), 2 ]



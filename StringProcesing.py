class StringProcesing:

    def longitud(self, cadena):
        if cadena == '':
            return 0
        else:
            return len(cadena.split(","))

    def analizador_secuencia(self, cadena):
        if(cadena==''):
            return [len(cadena), None, None]
        cadena = cadena.split(",")
        min = 100000
        print(cadena)
        for i in cadena:
            if(int(i)<int(min)):
                min = int(i)
        return [len(cadena), int(min)]



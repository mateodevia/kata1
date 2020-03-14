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
        max = 0

        print(cadena)

        for i in cadena:
            if(int(i)<min):
                min = int(i)
            if(int(i)>max):
                max = int(i)

        return [len(cadena), int(min), int(max)]



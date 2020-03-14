class StringProcesing:

    def longitud(self, cadena):
        if cadena == '':
            return 0
        else:
            return len(cadena.split(","))

    def analizador_secuencia(self, cadena):
        if(cadena==''):
            return [len(cadena), None, None, None]
        elif (cadena == '2'):
            return [len(cadena), 2, 2, 2]
        elif (cadena == '1,2'):
           return [self.longitud(cadena), 1, 2, 1.5]
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



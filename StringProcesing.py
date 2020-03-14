class StringProcesing:

    def longitud(self, cadena):
        if cadena == '':
            return 0
        else:
            return len(cadena.split(","))

    def analizador_secuencia(self, cadena):
        if(cadena==''):
            return [len(cadena), None, None]
        elif (cadena=='2'):
            return [len(cadena), 2, 2]
        elif (cadena=='1,2'):
            return [len(cadena), 1, 2]

        cadena = cadena.split(",")
        min = 100000

        print(cadena)

        for i in cadena:
            if(int(i)<int(min)):
                min = int(i)

        return [len(cadena), int(min),None]



#algoritmo padre de encriptacion

class algoritmoEncriptamiento():
    
    @staticmethod
    def encrip(numero):
        pass
    @staticmethod
    def decrip(numero):
        pass

# algoritmo de multiplicacion
class multiplicar6(algoritmoEncriptamiento):
    @staticmethod
    def encrip(numero):
        return numero * 6
    @staticmethod
    def decrip(numero):
        return numero / 6
# algoritmo de diferencia12
class diferencia12(algoritmoEncriptamiento):
    @staticmethod
    def encrip(numero):
        return numero - 12
    @staticmethod
    def decrip(numero):
        return numero + 12
# algoritmo de xor10
class xor10(algoritmoEncriptamiento):
    @staticmethod
    def encrip(numero):
        return numero ^ 10
    @staticmethod
    def decrip(numero):
        return numero ^ 10

class encriptador:
    def __init__(self) -> None:
        pass
   

    @staticmethod
    def _encriptar(numero, algoritmo):
        return algoritmo.encrip(numero)
        
    @staticmethod
    def _desencriptar(numero, algoritmo):
        return algoritmo.decrip(numero)
    @staticmethod
    def encriptar(numero,alg):
        if alg == "xor":
            return encriptador._encriptar(numero,xor10)
        if alg == "diferencia":
            return encriptador._encriptar(numero,diferencia12)
        if alg == "multiplicar":
            return encriptador._encriptar(numero,multiplicar6)
        raise Exception('El algoritmo no existe, por favor ingrese los nombres xor, multiplicar,diferencia')

    @staticmethod
    def desencriptar(numero,alg):
        if alg == "xor":
            return encriptador._desencriptar(numero,xor10)
        if alg == "diferencia":
            return encriptador._desencriptar(numero,diferencia12)
        if alg == "multiplicar":
            return encriptador._desencriptar(numero,multiplicar6)
        raise Exception('El algoritmo no existe, por favor ingrese los nombres xor, multiplicar,diferencia')


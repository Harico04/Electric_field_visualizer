
class Carga:
    
    def __init__(self, x, y, signo = 1):
        self.x = x
        self.y = y
        self.signo = signo
        self.valorCarga=1e-9 * signo

    def Valor(self):
        return self.valorCarga

    def X(self):
        return self.x
    
    def Y(self):
        return self.y
    
    def Signo(self):
        return self.signo
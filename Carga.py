
class Carga:
    
    def __init__(self,signo,x,y) -> None:
        self.valorCarga=1.609e-19 * signo
        self.x=x
        self.y=y
        self.signo = signo
    
    def X(self):
        return self.x
    
    def Y(self):
        return self.y
    
    def Signo(self):
        return self.signo

    def valor(self):
        return self.valorCarga
    

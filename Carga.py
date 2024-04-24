
class Carga:
    
    def __init__(self,signo,x,y) -> None:
        self.carga=1.609e-19
        self.x=x
        self.y=y
        if(signo=='-'):
           self.tipo=-1
        else:
            self.tipo=1
    
    def Magnitud(self):
        return self.carga
    
    def X(self):
        return self.x
    
    def Y(self):
        return self.y
    
    def Signo(self):
        return self.tipo
    

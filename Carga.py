
class Carga:

    def __init__(self,signo,x,y) -> None:
        self.carga=1.609e-19
        self.x=x
        self.y=y
        if(signo=='-'):
           self.tipo='-'
        else:
            self.tipo='+'
    
    def getMagnitudCarga(self):
        return self.carga
    
    def getX(self):
        return self.x
    
    def getY(self):
        return self.y
    
    def getTipo(self):
        return self.tipo
    

import matplotlib.pyplot as plt

class Carga:
    
    def __init__(self,signo,x,y) -> None:
        self.valorCarga=1.609e-19 * signo
        self.x=x
        self.y=y
        self.signo = signo
        self.dibujo=plt.Circle((self.x,self.y),0.2,color = 'red' if self.tipo == 1 else 'blue',fill=True,picker=True)
    
    def Magnitud(self):
        return self.carga
    
    def X(self):
        return self.x
    
    def Y(self):
        return self.y
    
    def Signo(self):
        return self.signo

    def valor(self):
        return self.valorCarga
    
    def Dibujo(self):
        return self.dibujo

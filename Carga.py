import matplotlib.pyplot as plt

class Carga:
    
    def __init__(self,signo,x,y) -> None:
        self.carga=1.609e-19
        self.x=x
        self.y=y
        if(signo=='-'):
           self.tipo=-1
        else:
            self.tipo=1
        self.dibujo=plt.Circle((self.x,self.y),0.2,color = 'red' if self.tipo == 1 else 'blue',fill=True,picker=True)
    
    def Magnitud(self):
        return self.carga
    
    def X(self):
        return self.x
    
    def Y(self):
        return self.y
    
    def Signo(self):
        return self.tipo
    
    def Dibujo(self):
        return self.dibujo

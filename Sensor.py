import matplotlib.pyplot as plt

class Sensor:
    def __init__(self,x,y,i,j):
        self.x=x
        self.y=y
        self.dibujo=plt.Circle((self.x,self.y),0.1,color = 'yellow',fill=True,picker=True)
        self.vector_i=i
        self.vector_j=j

    def modificarPosicion(self,x,y):
        self.x=x
        self.y=y
        self.dibujo.center=(x,y)
        
    def modificarVector(self,i,j):
        self.vector_i=i
        self.vector_j=j

    def X(self):
        return self.x

    def Y(self):
        return self.y
    
    def Dibujo(self):
        return self.dibujo
    
    def componenteI(self):
        return self.vector_i
    
    def componenteJ(self):
        return self.vector_j
    
    def manitudVector(self):
        return (self.vector_j**2+self.vector_i**2)**(1/2)
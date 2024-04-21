#AUN NO ESTA EN USO
#AUN NO ESTA EN USO
#AUN NO ESTA EN USO

class Vector:
    #atributos(bidimensionales por simplicidad)
    x=0
    y=0
    #metodos
    def __init__(self,x,y) -> None:
        self.x=x
        self.y=y

    #************************************
    def norma(self):
        for i in self.componentes:
            suma+=i
        return suma**(1/2)
    
    #************************************
    def x(self):
        return self.x
    
    #************************************
    def y(self):
        return self.y
    
    #************************************
    def normalizar(self):
        norma=self.norma()
        unitario=Vector(self.x/norma,self.y/norma)
        return unitario
    
    #************************************

    

        
    
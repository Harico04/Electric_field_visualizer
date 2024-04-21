import matplotlib.pyplot as plt
import numpy as np
from Carga import Carga

class Campo:

    k=9e9
    #*************************************************************************
    def __init__(self):
        self.horizontal=np.linspace(-5,5,16)
        self.vertical=np.linspace(-5,5,16)
        (self.horizontal,self.vertical)=np.meshgrid(self.horizontal,self.vertical)
        self.cargas=[]
        self.vector_i = np.zeros_like(self.horizontal)
        self.vector_j = np.zeros_like(self.vertical)
        self.actualizarVectores()
        
    #*************************************************************************
    def actualizarVectores(self):
        #Reiniciar los vectores
        self.vector_i.fill(0)  # Reiniciar los vectores a cero
        self.vector_j.fill(0)

        # Calcular los vectores en función de las coordenadas de la carga
        for cargaActual in self.cargas:
            self.vector_i += ((self.k * cargaActual.getMagnitudCarga()) / ((self.horizontal - cargaActual.getX())**2 + (self.vertical - cargaActual.getY())**2)**(3/2)) * (self.horizontal - cargaActual.getX())
            self.vector_j += ((self.k * cargaActual.getMagnitudCarga()) / ((self.horizontal - cargaActual.getX())**2 + (self.vertical - cargaActual.getY())**2)**(3/2)) * (self.vertical-cargaActual.getY())
        
        # Normalizar los vectores
        vector_magnitud = (self.vector_i**2 + self.vector_j**2)**(1/2)
        self.vector_i = self.vector_i / vector_magnitud
        self.vector_j = self.vector_j / vector_magnitud

    #*************************************************************************
    def crearCarga(self,event,ax):#event hace que este metodo sea un escuchador

        #Obtener coordenadas del click(por el momento todas las cargas son positivas)
        cargaActual=Carga('+',event.xdata,event.ydata)
        self.cargas.append(cargaActual)

        #Actualizar los vectores al haber una carga nueva a considerar
        self.actualizarVectores()

        #Actualizar el plot
        ax.clear()
        ax.quiver(self.horizontal, self.vertical, self.vector_i, self.vector_j, color='white')

        #Dibujar todas las cargas
        for cargaIterada in self.cargas:
            dibujoCarga=plt.Circle((cargaIterada.getX(),cargaIterada.getY()),0.2,color='red',fill=True)
            ax.add_patch(dibujoCarga)

        ax.set_xlabel('x')
        ax.set_ylabel('y')
        plt.draw()



        

    
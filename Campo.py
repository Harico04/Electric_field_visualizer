import matplotlib.pyplot as plt
import numpy as np
from Carga import Carga

class Campo:

    k=9e9
    #*************************************************************************
    def __init__(self):
        self.horizontal=np.linspace(-5,5,11)
        self.vertical=np.linspace(-5,5,11)
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
        for q in self.cargas:
            vector_magnitud = ((self.horizontal - q.X())**2 + (self.vertical - q.Y())**2)**(3/2)
            if(vector_magnitud == 0).any() : vector_magnitud = 0.000001 #Evitar divisiones por cero.
            
            self.vector_i += self.k * q.Signo() * q.Magnitud() / vector_magnitud * (self.horizontal - q.X())
            self.vector_j += self.k * q.Signo() * q.Magnitud() / vector_magnitud * (self.vertical - q.Y())
        
        # Normalizar los vectores
        vector_magnitud = np.sqrt(self.vector_i**2 + self.vector_j**2)
        self.vector_i = self.vector_i / vector_magnitud
        self.vector_j = self.vector_j / vector_magnitud

    #*************************************************************************
    def crearCarga(self,event,ax):#event hace que este metodo sea un escuchador

        if event.button == 1:  # Botón izquierdo
            tipo_carga = '+'
        elif event.button == 3:  # Botón derecho
            tipo_carga = '-'
        else:
            return  # Ignora otros botones como el botón central
        
        #Obtener coordenadas del click
        cargaActual=Carga(tipo_carga,event.xdata,event.ydata)
        self.cargas.append(cargaActual)

        #Actualizar los vectores al haber una carga nueva a considerar
        self.actualizarVectores()

        #Actualizar el plot
        ax.clear()
        ax.quiver(self.horizontal, self.vertical, self.vector_i, self.vector_j, color='white')

        #Dibujar todas las cargas
        for q in self.cargas:
            ax.add_artist(q.Dibujo())

        ax.set_xlabel('x')
        ax.set_ylabel('y')
        plt.draw()
    #*************************************************************************
    def moverCarga(self,event,fig):
        #Checar si alguna carga se selecciono
        for q in self.cargas:
            if event.artist==q.Dibujo():

                #Escuchador que cambia la posicion de la carga
                def mover(event):
                    q.Dibujo().center=(event.xdata,event.ydata)
                    self.actualizarVectores()
                    fig.canvas.draw_idle()

                #Conectar el evento de movimiento al plot
                id_movimiento=fig.canvas.mpl_connect('motion_notify_event',mover)

                # Desconectar el evento de movimiento después de soltar el botón del ratón
                def soltar(event):
                    fig.canvas.mpl_disconnect(id_movimiento)
                
                #Conectar el evento de desconexion al plot
                fig.canvas.mpl_connect('button_release_event', soltar)
                
                #romper el ciclo
                break




        

    

import matplotlib.pyplot as plt
import numpy as np
from Carga import Carga


# Esta clase se encarga de hacer los cálculos del campo eléctrico, así como
# el dibujar las cargas del campo eléctrico.

class Campo:

    k=9e9
    
    #*************************************************************************
    def __init__(self, ax):

        # Como se dibujará el campo eléctrico.  
        self.horizontal=np.linspace(-5,5,16)
        self.vertical=np.linspace(-5,5,16)
    def __init__(self):
        self.horizontal=np.linspace(-5,5,11)
        self.vertical=np.linspace(-5,5,11)
        (self.horizontal,self.vertical)=np.meshgrid(self.horizontal,self.vertical)

        # El conjunto de cargas que tendrá este campo eléctrico.
        self.cargas=[]

        # El conjunto de vectores unitarios que nos dirán como se
        # comporta el campo eléctrico.
        self.vector_i = np.zeros_like(self.horizontal)
        self.vector_j = np.zeros_like(self.vertical)

        self.ax = ax

        # Conectar el escuchador de eventos de clic del ratón
        self.ax.figure.canvas.mpl_connect('button_press_event', self.actualizarCampo)



    # ***********************************************************************
    # Se encarga de actualizar el conjunto de vectores unitarios en función
    # del conjunto de cargas que existen. 
    def actualizarVectores(self):
        
        #Reiniciar los vectores a cero
        self.vector_i.fill(0) 
        self.vector_j.fill(0)

        # Calcular los vectores en función de las cargas existentes.
        for q in self.cargas:
            vector_magnitud = ((self.horizontal - q.X())**2 + (self.vertical - q.Y())**2)**(3/2)
            if(vector_magnitud == 0).any() : vector_magnitud = 0.000001 #Evitar divisiones por cero.
            
            self.vector_i += self.k * q.valor() / vector_magnitud * (self.horizontal - q.X())
            self.vector_j += self.k * q.valor() / vector_magnitud * (self.vertical - q.Y())
        
        # Normalizar el conjunto de vectores del campo.
        vector_magnitud = np.sqrt(self.vector_i**2 + self.vector_j**2)
        self.vector_i = self.vector_i / vector_magnitud
        self.vector_j = self.vector_j / vector_magnitud

    #*************************************************************************
    # Agrega una carga al conjunto de cargas del campo.
    def agregarCarga(self, x, y):
        cargaActual=Carga(1, x, y)
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
        
        
    #*************************************************************************
    # Se encarga de actualizar el campo.
    # Se llama a llamar sola ya que es un escuchador.
    def actualizarCampo(self, event): 

        #Agrega una carga.
        self.agregarCarga(event.xdata, event.ydata)

        # Actualizar los vectores al haber una carga nueva a considerar
        self.actualizarVectores()

        # Dibuja a las cargas así como a los vectores actualizados.
        self.redibujar()

    #*************************************************************************
    # Se encarga de volver a dinujar el conjunto de vectores y de cargas
    # del campo eléctrico.
    def redibujar(self):
        self.ax.clear()
        self.ax.quiver(self.horizontal, self.vertical, self.vector_i, self.vector_j, color='white')
        for q in self.cargas:
            self.ax.add_artist(q.Dibujo())

        self.ax.set_xlabel('x')
        self.ax.set_ylabel('y')
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




        

    

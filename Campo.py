import matplotlib.pyplot as plt
import numpy as np
from Carga import Carga
from matplotlib.widgets import RadioButtons
from Sensor import Sensor

# Esta clase se encarga de hacer los cálculos del campo eléctrico, así como
# el dibujar las cargas del campo eléctrico.

class Campo:

    k=9e9
    cargaSeleccionada=False #Para checar si se esta queriendo mover una carga, moverCarga() se llama antes que actualizarCampo()
    sensorSeleccionado=False #Para checar si se tiene seleccionada la opcion de sensor en el RadioButton
    #*************************************************************************
    def __init__(self, ax, radio_ax):

        # Como se dibujará el campo eléctrico.  
        self.horizontal=np.linspace(-5,5,16)
        self.vertical=np.linspace(-5,5,16)
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
        self.ax.figure.canvas.mpl_connect('pick_event', self.moverCarga)
        self.ax.figure.canvas.mpl_connect('pick_event', self.movimientoSensor)
        #Guarda una referencia al dibujo del sensor
        self.sensor=Sensor(0,0,0,0)

        # Configuración de los Radio Buttons
        self.radio_ax = radio_ax
        self.radio_button = RadioButtons(self.radio_ax, ('+', '-','Sensor'))
        self.carga_signo = 1  # Signo inicial de la carga

        # Actualizar el signo de la carga cuando se selecciona un radio button
        self.radio_button.on_clicked(self.seleccionarDibujado)

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
        cargaActual=Carga(self.carga_signo, x, y)
        self.cargas.append(cargaActual)
    #*************************************************************************
    # Se encarga de actualizar el campo.
    # Se llama a llamar sola ya que es un escuchador.
    def actualizarCampo(self, event): 

        # No hacer nada si el click no esta en el área del campo eléctrico.
        if event.inaxes != self.ax: return
        
        #checa que no se este intentado colocar un sensor
        if self.sensorSeleccionado: return

        #Agrega una carga si no se tiene una seleccionada.
        if(self.cargaSeleccionada):
            self.cargaSeleccionada=False
        else:
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

        if self.sensorSeleccionado:
            self.ax.add_artist(self.sensor.Dibujo())
            self.ax.quiver(self.sensor.X(),self.sensor.Y(),self.sensor.componenteI(),self.sensor.componenteJ(),color='red')

        self.ax.set_xlabel('x')
        self.ax.set_ylabel('y')
        plt.draw()
    #*************************************************************************
    def moverCarga(self,event):
        #Checar si alguna carga se selecciono
        for q in self.cargas:
            if event.artist==q.Dibujo():
                self.cargaSeleccionada=True
                #Escuchador que cambia la posicion de la carga
                def mover(event):
                    q.modificarPosicion(event.xdata,event.ydata)
                    if(q.X()==None or q.Y()==None):
                        self.cargas.remove(q)
                    self.actualizarVectores()
                    self.redibujar()

                #Conectar el evento de movimiento al plot
                id_movimiento=self.ax.figure.canvas.mpl_connect('motion_notify_event',mover)

                # Desconectar el evento de movimiento después de soltar el botón del ratón
                def soltar(event):
                    self.ax.figure.canvas.mpl_disconnect(id_movimiento)

                #Conectar el evento de desconexion al plot
                self.ax.figure.canvas.mpl_connect('button_release_event', soltar)
                
                #rompe el ciclo
                break
    
    #*************************************************************************   
    def movimientoSensor(self,event):
        if event.artist!=self.sensor.Dibujo(): return
        def moverSensor(event):
            self.sensor.modificarPosicion(event.xdata,event.ydata)

            if self.sensor.X()==None or self.sensor.Y()==None:
                self.sensor.modificarPosicion(0,0)
                self.sensor.modificarVector(0,0)
                return
            
            campoEnX=0
            campoEnY=0
            for q in self.cargas:
                vector_magnitud=((self.sensor.X() - q.X())**2 + (self.sensor.Y() - q.Y())**2)**(3/2)
                campoEnX+=self.k * q.valor() / vector_magnitud * (self.sensor.X() - q.X())
                campoEnY+=self.k * q.valor() / vector_magnitud * (self.sensor.Y() - q.Y())

            self.sensor.modificarVector(campoEnX,campoEnY)
            print('<'+str(self.sensor.componenteI())+', '+str(self.sensor.componenteJ())+'>')
            self.redibujar()

        id_movimiento=self.ax.figure.canvas.mpl_connect('motion_notify_event', moverSensor)

        def soltarSensor(event):
            self.ax.figure.canvas.mpl_disconnect(id_movimiento)

        self.ax.figure.canvas.mpl_connect('button_release_event', soltarSensor)

    #*************************************************************************        
    # Cambia el dibujo realizado dependiendo de la opción seleccionada en el radiobutton.
    def seleccionarDibujado(self, label):
       if label=='+':
           self.carga_signo=1
           self.sensorSeleccionado=False
           self.redibujar()

       if label=='-':
           self.carga_signo=-1
           self.sensorSeleccionado=False
           self.redibujar()

       if label=='Sensor': 
           self.sensorSeleccionado=True
           self.redibujar()
           
    
        

    

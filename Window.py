import tkinter as tk
import Sistema
import Carga

class Window(tk.Tk):
    
    radio = 10

    def __init__(self):
        super().__init__()

        # Titulo de la ventana
        self.title("Simulador de campo eléctrico")

        # Configuración de la ventana
        self.resizable(False, False)
        self.config_width = 800
        self.config_height = 600

        # Configuracion de las opciones de visualización
        self.mostrar_lineas_campo = tk.BooleanVar()
        self.mostrar_equipotenciales = tk.BooleanVar()


        # Cargar cargas por defecto
        self.sistema = Sistema.Sistema()
        q1 = Carga.Carga(100, 300, 1)
        self.sistema.agregarCarga(q1)
        q2 = Carga.Carga(700, 300, -1)
        self.sistema.agregarCarga(q2)
        
        # Crear el canvas para dibujar las cargas
        self.canvas = tk.Canvas(self, width=self.config_width, height=self.config_height,
            bg='black')
        
        # Crear panel lateral
        self.panel = panel_lateral(self.sistema, 
            (self.mostrar_lineas_campo, self.mostrar_equipotenciales), 
            (self.cargaPositiva, self.cargaNegativa, self.sensor),
            self, bd=0, highlightthickness=0)
        
        # Configuracion predeterminada de visualización
        self.mostrar_lineas_campo.set(True)
        self.mostrar_equipotenciales.set(False)
        
        # Mostrar campo eléctrico
        self.mostrar_campo(self.sistema)

        # Mostrar cargas
        self.mostrar_cargas(self.sistema)

        # Empaqueta los widgets en la ventana
        self.canvas.pack(side=tk.LEFT)
        self.panel.pack(side=tk.RIGHT)

        # Actualizar el sistema
        self.canvas.tag_raise("carga")

    def cargaPositiva(self):
        q = Carga.Carga(self.x, self.y, 1)
        Sistema.sistema.agregarCarga(q)
        self.mostrar_cargas(self.sistema)
        self.refrescar_cargas()

    def cargaNegativa(self):
        q = Carga.Carga(self.x, self.y, -1)
        Sistema.sistema.agregarCarga(q)
        self.mostrar_cargas(self.sistema)
        self.refrescar_cargas()

    def sensor(self):
        p = Carga.Carga(self.x, self.y, 0)
        Sistema.sistema.agregarCarga(p)
        self.mostrar_cargas(self.sistema)
        self.refrescar_cargas()
    
    # eliminar carga si se da click derecho en una carga
    def eliminarCarga(self):
        for carga in self.sistema.obtenerCargas():
            if self.x == carga.X() and self.y == carga.Y():
                Sistema.sistema.eliminarCarga(carga)
                break
    
    
    def actualizarSistema(self):
        # Obtener posición del mouse
        mouse_x = self.canvas.winfo_pointerx() - self.canvas.winfo_rootx()
        mouse_y = self.canvas.winfo_pointery() - self.canvas.winfo_rooty()

        # Actualizar coordenadas de las cargas
        for carga in self.sistema.obtenerCargas():
            carga.x = self.canvas.coords(carga)[0] + self.radio
            carga.y = self.canvas.coords(carga)[1] + self.radio

        # Actualizar campo eléctrico
        self.canvas.delete("campo")
        self.mostrar_campo(self.sistema)


    def moverCarga(self):
        pass

    def dibujarEquipotenciales(self):
        pass
    
    def mostrar_campo(self, sistema):
        vectores_separacion = 50

        # Dibujar los vectores del campo eléctrico
        for i in range(self.config_width // vectores_separacion):
            for j in range(self.config_height // vectores_separacion):

                x = i * vectores_separacion
                y = j * vectores_separacion

                v = self.sistema.campoElectrico(x, y)

                # Normalizar el vector
                magnitud = self.sistema.distancia([0, 0], v)/30
                if magnitud != 0:
                    v[0] /= magnitud
                    v[1] /= magnitud

                # Dibujar el campo eléctrico
                vector = self.canvas.create_line(x, y, x + v[0], y + v[1],
                    fill="white", arrow=tk.LAST)

                self.canvas.addtag_withtag("campo", vector)


    def mostrar_cargas(self, sistema):
        for carga in self.sistema.obtenerCargas():
            if carga.Signo() == 1:
                color = "red"
            elif carga.Signo() == -1:
                color = "blue"
            else:
                color = "yellow"

            # Dibujar la carga
            p = self.canvas.create_oval(carga.X() - self.radio, carga.Y() - self.radio,
                carga.X() + self.radio, carga.Y() + self.radio, outline=color, fill=color)
            
            self.canvas.addtag_withtag("carga", p)

    def refrescar_campo(self):
        self.canvas.delete("campo")
        self.mostrar_campo(self.sistema)

    def refrescar_cargas(self):
        self.canvas.delete("carga")
        self.mostrar_cargas(self.sistema)

class panel_lateral(tk.Frame):
    def __init__(self, campo,casillas, botones, *args, **kwargs):
        super().__init__()

        self.x_etiqueta = tk.StringVar()
        self.y_etiqueta = tk.StringVar()
        self.campo_etiqueta = tk.StringVar()

        self.x_etiqueta = tk.Label(self, textvariable=self.x_etiqueta, width=15)
        self.y_etiqueta = tk.Label(self, textvariable=self.y_etiqueta, width=15)
        self.campo_etiqueta = tk.Label(self, textvariable=self.campo_etiqueta, width=30)

        self.campo_casilla = tk.Checkbutton(self, text="Campo electrico", variable = casillas[0])
        self.equipotenciales_casillas = tk.Checkbutton(self, text="Lineas equipotenciales", variable = casillas[1])

        self.btn_positiva = tk.Button(self, text="Agregar carga positiva")
        self.btn_negativa = tk.Button(self, text="Agregar carga negativa")
        self.btn_sensor = tk.Button(self, text="Agregar sensor")

        self.x_etiqueta.grid(row=0, column=0)
        self.y_etiqueta.grid(row=0, column=1)
        self.campo_etiqueta.grid(row=1, column=0, columnspan=2)
        self.campo_casilla.grid(row=2, column=0, columnspan=2)
        self.equipotenciales_casillas.grid(row=3, column=0, columnspan=2)
        self.btn_positiva.grid(row=4, column=0, columnspan=2)
        self.btn_negativa.grid(row=5, column=0, columnspan=2)
        self.btn_sensor.grid(row=6, column=0, columnspan=2)

        self.campo = campo
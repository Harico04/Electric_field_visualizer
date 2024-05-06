import Carga
import math


# Esta clase se encarga de hacer los cálculos del campo eléctrico, así como
# el dibujar las cargas del campo eléctrico.

class Sistema:
    def __init__ (self):
        self.cargas = []
    
    # Agrega una carga al conjunto de cargas del campo.
    def agregarCarga(self, carga):
        self.cargas.append(carga)

    def eliminarCarga(self, carga):
        self.cargas.remove(carga)
    
    def obtenerCargas(self):
        return self.cargas
    
    def distancia(self, a, b):
        return math.sqrt((a[0] - b[0])**2 + (a[1] - b[1])**2)
    
    # Se encarga de actualizar el conjunto de vectores unitarios en función
    # del conjunto de cargas que existen. 
    def campoElectrico(self, x, y, k=9e9):
        # Vector de campo eléctrico (i, j)
        vector_campo = [0, 0]

        # Encontrar el campo neto en una posición
        for carga in self.cargas:
            if carga.Signo() == 0:
                continue

            # Obtener la posición de la carga
            posicion_carga = (carga.X(), carga.Y())

            # Obtener la distancia a la carga
            distancia = self.distancia((x, y), posicion_carga)
            
            # Obtener la magnitud del campo eléctrico con Ley de Coulomb
            try:
                E  = k * carga.Valor() / (distancia ** 2)
            except ZeroDivisionError:
                return [0, 0]
            
            # Calcular los componentes del vector de campo
            vector_campo[0] += E * (carga.X() - x)
            vector_campo[1] += E * (carga.Y() - y)

        return vector_campo
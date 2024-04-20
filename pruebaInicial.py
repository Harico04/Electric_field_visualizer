import numpy as np
import matplotlib.pyplot as plt

#"horizontal" y "vertical" son los rangos de la grafica. ambos ejes van de -10 a 10.
#linspace hace que x,y sean arreglos que contienen 21 elementos del -10 al 10 separados de forma equitativa
#([-10,-9,-8,...,8,9,10]) 
horizontal=np.linspace(-5,5,11)
vertical=np.linspace(-5,5,11)

#meshgrid toma los arreglos x,y y los convierte en "grids" de 2x2, "con cantidad de valores en x" filas donde cada una es el arreglo original x. lo mismo para y.
#(si no se entiende manden x o y a imprimir para que lo vean)
(horizontal,vertical)=np.meshgrid(horizontal,vertical)
#posiciones de la carga
carga_x=float(input("Introduzca la posicion x de la carga[-10,10]: "))
carga_y=float(input("Introduzca la posicion y de la carga[-10,10]: "))
#constantes(por ahora)
k=1
q=1

#"vector_i" y "vector_j" son las componentes de los vectores que se estan graficando
vector_i=((k * q)/((horizontal - carga_x)**2+(vertical - carga_y)**2)**(3/2))*(horizontal - carga_x)
vector_j=((k * q)/((horizontal - carga_x)**2+(vertical - carga_y)**2)**(3/2))*(vertical - carga_y)
#normalizacion de los vectores, para que la grafica muestre solo direccion
vector_magnitud=(vector_i**2+vector_j**2)**(1/2)
vector_i=vector_i/vector_magnitud
vector_j=vector_j/vector_magnitud

#le pone los labels a cada eje
plt.xlabel('x')
plt.ylabel('y')


#quiver hace el campo vetorial. como x y y son meshgrids, coloca un vector con componentes <i,j> en cada configuracion de posiciones (x,y)
#((-10,10),(-9,10),(-8,10),...,(10,10))
#((-10,9,),(-9,9 ),(-8,9 ),...,(10,9 ))
#     .
#     .      .
#     .           .
#     .               .        
#     .                   .   
#     .                       .   
#     .                           .   
#((-10,10),(-0,10),(-8,-10),...,(10,-10))
plt.quiver(horizontal,vertical,vector_i,vector_j)
plt.show()
import matplotlib.pyplot as plt
from Campo import Campo


fig, ax=plt.subplots(figsize=(10,8))
campoVectorial=Campo(ax)
ax.quiver(campoVectorial.horizontal,campoVectorial.vertical,campoVectorial.vector_i,campoVectorial.vector_j,color='white')
plt.subplots_adjust(left=0,right=1,top=1,bottom=0)
ax.set_facecolor('black')
fig.set_facecolor('black')

<<<<<<< HEAD
#Activar el escuchador al hacer click
fig.canvas.mpl_connect('button_press_event', lambda event: campoVectorial.crearCarga(event,ax))
fig.canvas.mpl_connect('pick_event', lambda event: campoVectorial.moverCarga(event,fig))

plt.show()
=======
plt.show()
>>>>>>> 0e8cdb909b11cd95621f5509277ffac14b5ffae6

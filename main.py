import matplotlib.pyplot as plt
from Campo import Campo

fig, ax = plt.subplots(figsize=(10, 8))
plt.subplots_adjust(left=0.3, right=1, top=1, bottom=0)  # Ajustar para dejar espacio para los radio buttons

# Crear el área para los radio buttons
radio_ax = plt.axes([0.05, 0.7, 0.15, 0.15], facecolor='lightgoldenrodyellow')

# Inicialización de la clase Campo con el nuevo argumento
campoVectorial = Campo(ax, radio_ax)

# Dibujar el campo vectorial
ax.quiver(campoVectorial.horizontal, campoVectorial.vertical, campoVectorial.vector_i, campoVectorial.vector_j, color='white')
ax.set_facecolor('black')
fig.set_facecolor('black')

plt.show()
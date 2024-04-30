import matplotlib.pyplot as plt
from Campo import Campo


fig, ax=plt.subplots(figsize=(10,8))
campoVectorial=Campo(ax)
ax.quiver(campoVectorial.horizontal,campoVectorial.vertical,campoVectorial.vector_i,campoVectorial.vector_j,color='white')
plt.subplots_adjust(left=0,right=1,top=1,bottom=0)
ax.set_facecolor('black')
fig.set_facecolor('black')

plt.show()

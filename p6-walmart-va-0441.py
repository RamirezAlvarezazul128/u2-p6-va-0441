import matplotlib.pyplot as plt
import numpy as np
# Ramirez Azul NC 0441

cant_productos=[100,150,200,300,500]
precio = [4000,7000,9000,12000,18000]

plt.plot(cant_productos,precio)
plt.show()

## personaliza grafica
plt.plot(cant_productos,precio,color='pink',marker="o",linestyle='dashed',linewidth=2,markersize=12)
plt.title("ventas de walmart 0441")

plt.show()
plt.xlabel("cant prod")
plt.ylabel("precios")
plt.show()
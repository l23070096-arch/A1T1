import numpy as np
import matplotlib.pyplot as plt

lambda_llegadas = 4 
intervalos = 3   

llegadas = np.random.poisson(lambda_llegadas, intervalos)

print("Llegadas simuladas por intervalo de 5 minutos:")
print(llegadas)
print("Total de estudiantes en 15 minutos:", sum(llegadas))
#Grafica
plt.bar(range(1, intervalos+1), llegadas)
plt.xlabel("Intervalo (5 min)")
plt.ylabel("Número de estudiantes")
plt.title("Simulación de llegadas a la cafetería")
plt.show()

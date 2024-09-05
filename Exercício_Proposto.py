import numpy as np
import matplotlib.pyplot as plt

#Ar
h = 5 #W/m²*K

k = [0.055, 0.03] #W/m*K


#Cálculo do raio crítico
r_c1 = k[0]/h #m
r_c2 = k[1]/h #m

T_i = 77 #K
T_inf = 300 #K
r_i = 0.01 #m

def Taxa(r,k):
    return (T_inf-T_i)/(((np.log(r/r_i))/(2*np.pi*k))+((1)/(2*np.pi*r*h)))

x_axis = np.linspace(0.001, 0.05, 200)

q1 = []
q2 = []

for j in range(0, len(x_axis)):
    q1.append(Taxa(x_axis[j], k[0]))

for j in range(0, len(x_axis)):
    q2.append(Taxa(x_axis[j], k[1]))

plt.plot(x_axis, q1, color='r', label = 'k= 0.055')
plt.plot(x_axis, q2, color='g', label = 'k= 0.03')
plt.axvline(x=r_i, ymin=0, ymax=1, label = 'r_i = 0.01', color = 'grey', linestyle = 'dashed')
plt.axvline(x=r_c1, ymin=0, ymax=1, label = 'r_c1 = 0.011', color = 'red', linestyle = 'dashed', alpha = 0.5)
plt.axvline(x=r_c2, ymin=0, ymax=1, label = 'r_c2 = 0.006', color = 'green', linestyle = 'dashed', alpha = 0.5)

plt.xlabel("Raio de Isolamento (m)")
plt.ylabel("Taxa de Calor (W/m)")

plt.legend()

plt.show()

print(r_c1)
print(r_c2)
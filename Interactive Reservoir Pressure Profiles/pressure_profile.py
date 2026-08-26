# By: Nahil Nigar
# used AI to help me get the darcy radial flow equation into code correctly and to
# test it out. wrote/ran everything myself after.

import numpy as np
import matplotlib.pyplot as plt

q = float(input('flow rate q (STB/day): '))
k = float(input('permeability k (md): '))
h = float(input('reservoir thickness h (ft): '))
mu = float(input('fluid viscosity mu (cp): '))
pe = float(input('reservoir pressure at edge pe (psi): '))
rw = float(input('wellbore radius rw (ft): '))
re = float(input('drainage radius re (ft): '))

r = np.linspace(rw, re, 200)  # 200 points, curve looked smooth enough at this

p = pe - (q*mu/(0.00708*k*h))*np.log(re/r)

plt.figure(figsize=(7,5))
plt.plot(r,p,color='blue')
plt.xlabel('Radius (ft)')
plt.ylabel('Pressure (psi)')
plt.title('Reservoir Pressure Profile')
plt.grid(True)
plt.savefig('pressure_profile.png')
plt.show()

print('saved plot as pressure_profile.png')

# quick sensitivity check, comparing a few different permeabilities against each other
k_vals=[k*0.5, k, k*2]

plt.figure(figsize=(7,5))
for kt in k_vals:
    pt = pe - (q*mu/(0.00708*kt*h))*np.log(re/r)
    plt.plot(r, pt, label='k = '+str(kt)+' md')

plt.xlabel('Radius (ft)')
plt.ylabel('Pressure (psi)')
plt.title('Pressure Profile at Different Permeabilities')
plt.legend()
plt.grid(True)
plt.savefig('pressure_sensitivity.png')
plt.show()

print('saved sensitivity plot too')
